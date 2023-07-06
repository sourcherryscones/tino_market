from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from sqlalchemy.sql import func
app = Flask(__name__)
app.secret_key = "socrates"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:p9adm1n!@localhost:5432/tino_market_db'

db = SQLAlchemy(app)
# Post model

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300))
    year = db.Column(db.Integer, nullable=False)
    posted_by = db.Column(db.Integer, foreign_key=True)
    date_posted = db.Column(db.DateTime(timezone=True), server_default=func.now())
    recipient_id = db.Column(db.Integer, foreign_key=True)
    is_claimed = db.Column(db.Boolean, nullable=False)
    condition = db.Column(db.String(4), nullable=False)

    def __repr__(self):
        return f'<Student {self.title}>'

book_arr = [
    {
        'title': 'Barrons SAT Prep',
        'year': 2022,
        'claimed': False
    },
    {
        'title': 'Brightfox SAT Prep',
        'year': 2023,
        'claimed': False
    },
    {
        'title': 'Barrons APCSA Prep',
        'year': 2022,
        'claimed': True
    }
]



@app.route('/books')
def books():
    return book_arr

@app.route('/books/<int:id>')
def singlebooks(id):
    return book_arr[id]


if __name__ == '__main__':
    app.run(debug=True, host='192.168.15.224', port=5001)



