from flask import request, send_from_directory, jsonify, session, redirect, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, login_manager, current_user
from .models import db, Post, User
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail as sgmail
import os
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def loginpost():
    print('MADE IT TO LOGIN FUNCTION')
    req = request.json
    username = req['username']
    password = req['password']
    username_usr = User.query.filter_by(username=username).first()
    email_usr = User.query.filter_by(email=username).first()
    usr = username_usr if username_usr else email_usr
    if not usr:
        return jsonify({'success': False, 'error': 'USER NOT FOUND'})
    if not check_password_hash(usr.password, password):
        return jsonify({'success': False, 'error': 'INCORRECT PASSWORD'})

    #do actual checking of pw hash here
    login_user(usr,remember=False)
    return jsonify({'success': True})


@auth.route('/signup', methods=['POST']) # to be removed once /reg works as expected
def signup():
    requ = request
    req = request.get_json()
    email = req['email']
    username = req['username']
    password = req['password']
    grade = req['grade']
    pwconf = req['pwconf']
    usrcheck = User.query.filter_by(email=email).first()
    namecheck = User.query.filter_by(username=username).first()

    if usrcheck or namecheck:
        return jsonify({'registered': False, 'error': 'USER ALREADY EXISTS'})

    if password != pwconf:
        return jsonify({'registered': False, 'reguser': None, 'error': 'PASSWORDS DO NOT MATCH'})
    
    newusr = User(username=username, email=email, password=generate_password_hash(password, method='scrypt'), grade=grade)
    db.session.add(newusr)
    db.session.flush()
    db.session.commit()

    return jsonify({'registered': True})

@auth.route("/getsession")
def check_session():
    print("USER AUTHENTICATED? ")
    print(current_user.is_authenticated)
    if current_user.is_authenticated:
        return jsonify({"login": True})

    return jsonify({"login": False})

@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'logoutsuccessful': True})

# connect to frontend

@auth.route('/reg', methods=['POST'])
def create_unverified_user():
    req = request.get_json()
    email = req['email']
    username = req['username']
    password = req['password']
    grade = req['grade']
    pwconf = req['pwconf']
    usrcheck = User.query.filter_by(email=email).first()
    namecheck = User.query.filter_by(username=username).first()

    if usrcheck or namecheck:
        return jsonify({'registered': False, 'error': 'USER ALREADY EXISTS'})

    if password != pwconf:
        return jsonify({'registered': False, 'reguser': None, 'error': 'PASSWORDS DO NOT MATCH'})
    
    newvercode = random.randint(100000,999999)
    newusr = User(username=username, email=email, password=generate_password_hash(password, method='scrypt'), grade=grade, is_verified=False, verification_code=newvercode)
    db.session.add(newusr)
    db.session.flush()
    db.session.commit()
    print(newusr.asdict())

    msg = sgmail(
            from_email='tino.market.messenger@gmail.com',
            to_emails=email,
            subject='Verify your email & get started, ' + username + '!',
            html_content='Your code is '+ str(newvercode) + '! ' +'Please verify your email through <a href="https://tinomarket.org/#/verify/'+email+'/newuser">this</a> link :D')
    try:
        sg=SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(msg)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        print("message sent!")
    except Exception as e:
        print(e.message)

    return jsonify({'registered': True})

@auth.route('/verify', methods=['POST'])
def verify():
    req=request.get_json()
    print("REQ IS")
    print(req)
    email=req['email']
    code=req['code']
    fr=req['from']
    usr = User.query.filter_by(email=email).first()
    print(usr)
    print(usr.is_verified)

    if not usr:
        return jsonify({'verified': False, 'error': 'USER NOT FOUND'})
    
    if not usr.verification_code == code:
        return jsonify({'verified': False, 'error': 'WRONG CODE'})
    
    usr.is_verified = True
    usr.verification_code = -1
    db.session.commit()
    db.session.flush()

    return jsonify({'verified':True})


@auth.route('/emailver', methods=['POST'])
def email_ver():
    req = request.get_json()
    email = req['email']

    usr = User.query.filter_by(email=email).first()
    if not usr:
        return jsonify({'isindb': False})
    
    print("THIS USER IS LEGIT")
    print(email)

    newvercode = random.randint(100000,999999)

    usr.verification_code = newvercode
    db.session.commit()

    msg = sgmail(
            from_email='tino.market.messenger@gmail.com',
            to_emails=email,
            subject='Password reset request for ' + usr.username + '',
            html_content='Your code is '+ str(newvercode) + '! ' +'Please verify your email through <a href="https://tinomarket.org/#/verify/'+email+'/pwreset'+'">this</a> link :D')
    try:
        sg=SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(msg)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        print("message sent!")
    except Exception as e:
        print(e.message)
    # create verification code here
    # send back true, so we will navigate to /verify/pmarf/pwreset
    # now that thats happened, we can just verify if the thing in the db is the same as the one it's given!

    return jsonify({'isindb': True})


@auth.route('/reset', methods=['POST'])
def reset_pw():
    req = request.get_json()
    email = req['email']
    usr = User.query.filter_by(email=email).first()
    
    if not usr:
        return jsonify({'successful_update': False, 'errors': 'USER DOES NOT EXIST'})
    
    usr.password = generate_password_hash(req['newpw'], method='scrypt')
    db.session.commit()

    return jsonify({'successful_update': True})