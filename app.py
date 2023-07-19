from flask import Flask, request, send_from_directory, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
app = Flask(__name__)
app.secret_key = "socrates"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:p9adm1n!@localhost:5432/tino_market_db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    validation = db.Column(db.String(50))
    grade = db.Column(db.Integer)

    def asdict(self):
        return {'id': self.id, 'username': self.username, 'grade': self.grade, 'validation': self.validation}


# Post model

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300))
    posted_by = db.Column(db.Integer, db.ForeignKey(User.id)) # db.ForeignKey(users.id)
    date_posted = db.Column(db.DateTime(timezone=True), server_default=func.now())
    recipient_id = db.Column(db.Integer, db.ForeignKey(User.id))
    is_claimed = db.Column(db.Boolean, nullable=False)
    condition = db.Column(db.String(4), nullable=False)

    donor = relationship('User', foreign_keys='Post.posted_by')
    recip = relationship('User', foreign_keys='Post.recipient_id')
    


    def asdict(self):
        base = {'id': self.id, 'title': self.title, 'description': self.description, 'posted_by': self.posted_by, 'date_posted': str(self.date_posted), 'recipient_id': self.recipient_id, 'is_claimed': self.is_claimed, 'condition': self.condition}
        if (self.donor != None):
            base['donor'] = self.donor.username
        if (self.recip != None):
            base['recip'] = self.recip.username
        return base

    def addmultiple():
        books = [
        {
            'title': 'Barrons SAT Prep 2022',
            'description': 'very standard SAT prep!',
            'is_claimed': False,
            'condition': 'OK'
        },
        {
            'title': 'Brightfox SAT Prep 2023',
            'description': 'fairly new, 10 practice tests!!',
            'is_claimed': False,
            'condition': 'GOOD'
        },
        {
            'title': 'Barrons APCSA Prep 2021',
            'description': 'good for review exercises, although a bit harder than the AP exam',
            'is_claimed': True,
            'condition': 'OK'
        }
        ]
        for b in books:
            bdict = Post(title=b['title'],description=b['description'], posted_by=0, recipient_id=1, is_claimed=b['is_claimed'], condition=b['condition'])
            db.session.add(bdict)
        db.session.commit()


@app.route('/postsquared', methods=['POST'])
def postsquared():
    jfather = request.json
    #print(jfather)
    #print(type(jfather))
    postified = Post(title=jfather['title'],description=jfather['description'], posted_by=jfather['posted_by'], is_claimed=jfather['is_claimed'], condition=jfather['condition'])
    db.session.add(postified)
    db.session.flush()
    db.session.commit()
    '''stmt = select(Post).where(Post.id == jfather.id)
    result = db.session.execute(stmt)
    '''
    db.session.refresh(postified) 
    result = Post.query.filter_by(id=postified.id).first()
    print("RESULT IS ", result.title, result.description)
    return f'{result.title} was added to the POSTS database!'

@app.route('/update/<int:id>', methods=['PUT'])
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

@app.route('/claim/<int:id>', methods=['PUT'])
def claimbook(id):
    tbu = Post.query.filter_by(id=id).first()
    jfather = request.json
    tbu.title = jfather['title']
    tbu.description = jfather['description']
    tbu.posted_by = jfather['posted_by']
    tbu.is_claimed = True
    tbu.recipient_id = 1
    tbu.condition = jfather['condition']
    db.session.commit()
    db.session.refresh(tbu)
    print(tbu.asdict())
    return tbu.asdict()
    


@app.route('/delete/<int:id>', methods=['DELETE'])
def deletebook(id):
    tbd = Post.query.filter_by(id=id).first()
    if tbd is None:
        return "Sorry, that title isn't in our database"
    deleted_title = tbd.title
    db.session.delete(tbd)
    db.session.commit()
    return f'{deleted_title} was deleted from the database!'
    

@app.route('/allposts')
def getposts():
    allposts = Post.query.all()
    tbr = []
    for p in allposts:
        dictp = p.asdict()
        tbr.append(dictp)
    return tbr

@app.route('/books/<int:id>')
def singlebooks(id):
    print(id, type(id))
    sb = Post.query.get(id)
    sb = sb.asdict()
    return sb

###################################################################################################################

@app.route('/createuser', methods=['POST'])
def newuser():
    req = request.json
    
    newuser = User(username=req['username'], password=req['password'], grade=req['grade'])
    db.session.add(newuser)
    db.session.flush()
    db.session.commit()
    #stmt = select(Post).where(Post.id == jfather.id)
    #result = db.session.execute(stmt)
    
    db.session.refresh(newuser)
    result = User.query.filter_by(id=newuser.id).first()
    print("RESULT IS ", result.username, result.grade)
    return f'{result.username} was added to the USERS database!'
# works


@app.route('/users/update/<int:id>', methods=['PUT'])
def userupdate(id):
    tbu = User.query.filter_by(id=id).first()
    jfather = request.json
    print(jfather)
    if (jfather['validation'] == tbu.password):
        tbu.username = jfather['username']
        tbu.password = jfather['password']
        tbu.validation = None,
        tbu.grade = jfather['grade']
        db.session.commit()
        return f'{tbu.username} was successfully updated!' 
    else:
        return "ERROR: invalid credentials :("
        #return redirect('/error')



@app.route('/users/delete/<int:id>', methods=['DELETE'])
def deluser(id):
    tbd = User.query.filter_by(id=id).first()
    print(tbd)
    deleted_name = tbd.username
    db.session.delete(tbd)
    db.session.commit()
    return f'{deleted_name} was deleted from the USERS database!'
    

@app.route('/users')
def get_all_users():
    allusers = User.query.all()
    tbr = []
    for u in allusers:
        dict_u = u.asdict()
        tbr.append(dict_u)
    return tbr

@app.route('/users/<int:id>')
def singleuser(id):
    su = Post.query.get(id)
    su = su.asdict()
    return su


# SVELTE STUFF
@app.route('/', methods=['GET'])
def base():
    return send_from_directory('client/public', 'index.html')

@app.route('/<path:path>')
def home(path):
    return send_from_directory('client/public', path)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)




