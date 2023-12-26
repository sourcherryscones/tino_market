import os
from flask import request, send_from_directory, jsonify, session, redirect, Blueprint, current_app
from .sthree import upload_file_to_s3, allowed_file, get_unique_filename
from werkzeug.security import generate_password_hash, check_password_hash
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail as sgmail
import boto3

from flask_login import login_required, current_user
from .models import db, Post
from marketflask import s3_client

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def base():
    print('made it to base!')
    return send_from_directory('../client/public', 'index.html')

@main.route('/<path:path>')
def home(path):
    return send_from_directory('../client/public', path)
'''
post categories: book, textbook, notebook, other
'''
@main.route('/postsquared', methods=['POST'])
@login_required
def postsquared():
    fdata = dict(request.form)
    dfltimg = False
    fyles = request.files
    if not fyles['postimg'].filename:
        dfltimg = True
        #return "<h1>Did not include image</h1>"
    
    if dfltimg == False:
        pimg = fyles['postimg']

        if not allowed_file(pimg.filename):
            return "<h1>Did not include proper image type</h1>"
        
        pimg.filename = get_unique_filename(pimg.filename)

        upload = upload_file_to_s3(s3_client, current_app.config['BUCKET_NAME'], pimg)

        print(upload)

        if 'url' not in upload:
            return "<h1>Upload failed D:</h1>"
        
        
        yourl = upload['url']
    else:
        if fdata['category'] == 'PREPBOOK':
            yourl = "/textbookicon.png"
        else:
            yourl = "/undrawnotesicon.png"
    print("YOURL IS")
    print(yourl)
    print(type(yourl))

    #update the db model thing
    
    print(fdata)
    postified = Post(title=fdata['title'],description=fdata['description'], posted_by=current_user.id, is_claimed=False, condition=fdata['condition'], image=yourl, category=fdata['category'])
    db.session.add(postified)
    db.session.flush()
    db.session.commit()
    db.session.refresh(postified) 
    result = Post.query.filter_by(id=postified.id).first()
    print("RESULT IS ", result.title, result.description)
    return redirect('/#/feed')


@main.route('/claim/<int:id>', methods=['PUT'])
@login_required
def claimbook(id):
    tbu = Post.query.filter_by(id=id).first()
    jfather = request.json
    tbu.title = jfather['title']
    tbu.description = jfather['description']
    tbu.posted_by = jfather['posted_by']
    tbu.is_claimed = True
    tbu.recipient_id = current_user.id
    tbu.condition = jfather['condition']
    db.session.commit()
    db.session.refresh(tbu)
    print(tbu.asdict())
    p=tbu
    dictp = tbu.asdict()
    if dictp['is_claimed'] == True:
            if (current_user.id == p.donor.id):
                dictp['recip_email'] = p.recip.email
            if (current_user.id == p.recip.id):
                dictp['donor_email'] = p.donor.email
            # SENDGRID THINGS
            msg = sgmail(
            from_email='tino.market.messenger@gmail.com',
            to_emails=[p.donor.email, p.recip.email],
            subject='Transaction complete!',
            html_content='<h1>Congratulations, ' + p.donor.username + ' and ' + p.recip.username + '!</h1><p>Your item <strong>'+ p.title +'</strong> has been claimed by ' + p.recip.username + ', who has been copied on this email so that you two can figure out meeting times!</p>'
            )
            try:
                sg=SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(msg)
                print(response.status_code)
                print(response.body)
                print(response.headers)
                print("message sent!")
            except Exception as e:
                print(e.message)
    return dictp

@main.route('/update/<int:id>', methods=['PUT'])
@login_required
def updatebook(id):
    tbu = Post.query.filter_by(id=id).first()
    jfather = request.json
    tbu.title = jfather['title']
    tbu.description = jfather['description']
    tbu.posted_by = jfather['posted_by']
    tbu.is_claimed = jfather['is_claimed']
    tbu.condition = jfather['condition']
    db.session.commit()
    db.session.refresh(tbu)
    return tbu.asdict()

#MAKE A BUTTON OR SOMETHING LMAO (same as the email, only available to user for their own items)
@main.route('/delete/<int:id>', methods=['DELETE'])
@login_required
def deletebook(id):
    tbd = Post.query.filter_by(id=id).first()
    if tbd is None:
        return "Sorry, that title isn't in our database"
    deleted_title = tbd.title
    db.session.delete(tbd)
    db.session.commit()
    return jsonify({'delbooksuccess': True})

@main.route('/allposts')
@login_required
def getposts():
    allposts = Post.query.filter_by(is_claimed=False)
    print(allposts)
    tbr = []
    for p in allposts:
        dictp = p.asdict()
        if dictp['is_claimed'] == True:
            if (current_user.id == p.donor.id):
                dictp['recip_email'] = p.recip.email
            if (current_user.id == p.recip.id):
                dictp['donor_email'] = p.donor.email
        tbr.append(dictp)
    #print(tbr)
    return tbr

@main.route('/myitems')
@login_required
def getmyitems():
    myid = current_user.id
    myposts = Post.query.filter_by(recipient_id=myid)
    print(myposts)
    tbr = []
    for p in myposts:
        dictp = p.asdict()
        if dictp['is_claimed'] == True:
            if (current_user.id == p.donor.id):
                dictp['recip_email'] = p.recip.email
            if (current_user.id == p.recip.id):
                dictp['donor_email'] = p.donor.email
        tbr.append(dictp)
    #print(tbr)
    return tbr

@main.route('/myposts')
@login_required
def getmyposts():
    myid = current_user.id
    myposts = Post.query.filter_by(posted_by=myid)
    print(myposts)
    tbr = []
    for p in myposts:
        dictp = p.asdict()
        if dictp['is_claimed'] == True:
            if (current_user.id == p.donor.id):
                dictp['recip_email'] = p.recip.email
            if (current_user.id == p.recip.id):
                dictp['donor_email'] = p.donor.email
        tbr.append(dictp)
    #print(tbr)
    return tbr

@main.route('/books/<int:id>')
@login_required
def singlebooks(id):
    print(id, type(id))
    sb = Post.query.get(id)
    sb = sb.asdict()
    return sb
