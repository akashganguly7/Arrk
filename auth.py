from flask import Blueprint, request, make_response
from Models.User import User
from werkzeug.security import generate_password_hash, check_password_hash
from run import db
from datetime import datetime
from http import HTTPStatus

auth = Blueprint('auth', __name__)


def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    if user:
        if check_password_hash(user.password, password):
            return make_response({'message': 'User Logged In'}), HTTPStatus.OK
        else:
            return make_response({'message': 'Incorrect Password'}), HTTPStatus.OK
    else:

        return make_response({'message': 'User not registered'}), HTTPStatus.OK

def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    user = User.query.filter_by(email=email).first()

    if user:
        return make_response({'message': 'User Already Present'}), HTTPStatus.FOUND
    else:
        user = User(email=email, username=username, password=generate_password_hash(password),
                    first_name=first_name, last_name=last_name, created_on=datetime.now())
        db.session.add(user)
        db.session.commit()
        return make_response({'message': 'User Added'}), HTTPStatus.CREATED

# @auth.route('/logout')
# def logout():
#     return 'Logout'
