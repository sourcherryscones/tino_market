from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from marketflask import login_manager
from flask_login import UserMixin
from sqlalchemy.orm import relationship
db = SQLAlchemy(engine_options={"pool_pre_ping": True, "pool_recycle":300})

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    grade = db.Column(db.Integer)
    is_verified=db.Column(db.Boolean, nullable=False)
    verification_code=db.Column(db.Integer)

    def asdict(self):
        return {'id': self.id, 'username': self.username, 'email': self.email, 'grade': self.grade, 'is_verified': self.is_verified, 'verification_code': self.verification_code}



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
    image = db.Column(db.String(100))
    category = db.Column(db.String(30))

    donor = relationship('User', foreign_keys='Post.posted_by')
    recip = relationship('User', foreign_keys='Post.recipient_id')
    


    def asdict(self):
        base = {'id': self.id, 'title': self.title, 'description': self.description, 'posted_by': self.posted_by, 'date_posted': str(self.date_posted), 'recipient_id': self.recipient_id, 'is_claimed': self.is_claimed, 'condition': self.condition, 'image': self.image, 'category': self.category}
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