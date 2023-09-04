from flask import request, send_from_directory, jsonify, session, redirect, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Message
from flask_login import login_user, logout_user, login_required, login_manager
from .models import db, Post, User

auth = Blueprint('auth', __name__)



@auth.route('/login', methods=['POST'])
def loginpost():
    print('MADE IT TO LOGIN FUNCTION')
    req = request.json
    username = req['username']
    password = req['password']
    usr = User.query.filter_by(username=username).first()
    print(usr.password)
    if not usr or not check_password_hash(usr.password, password):
        return jsonify({'success': False})

    #do actual checking of pw hash here
    login_user(usr,remember=False)
    return jsonify({'success': True})


@auth.route('/signup', methods=['POST'])
def signup():
    requ = request
    req = request.get_json()
    email = req['email']
    username = req['username']
    password = req['password']
    grade = req['grade']
    pwconf = req['pwconf']
    usrcheck = User.query.filter_by(email=email).first()

    if usrcheck:
        return jsonify({'registered': False, 'error': 'already exists'})

    if password != pwconf:
        return jsonify({'registered': False, 'reguser': None})
    
    newusr = User(username=username, email=email, password=generate_password_hash(password, method='scrypt'), grade=grade)
    db.session.add(newusr)
    db.session.flush()
    db.session.commit()

    return jsonify({'registered': True})


@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'logoutsuccessful': True})