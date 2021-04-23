from flask import Blueprint, request, make_response
from Models.User import User
from werkzeug.security import generate_password_hash, check_password_hash
from run import db
from datetime import datetime
from http import HTTPStatus

auth = Blueprint('auth', __name__)


def login():
    try:
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user: # checks if user present (valid scenario)
            if check_password_hash(user.password, password): # allows only if password hash matches
                return make_response({'message': 'User Logged In'}), HTTPStatus.OK
            else:
                return make_response({'message': 'Incorrect Password'}), HTTPStatus.OK
        else:

            return make_response({'message': 'User not registered'}), HTTPStatus.OK
    except Exception as e:
        return make_response({'message': 'Internal Server Error'}), HTTPStatus.BAD_REQUEST


def signup():
    try:
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')

        user = User.query.filter_by(username=username).first()

        if user:  # checks if user present
            return make_response({'message': 'User Already Present'}), HTTPStatus.FOUND
        else: # valid scenario
            user = User(email=email, username=username, password=generate_password_hash(password),
                        first_name=first_name, last_name=last_name, created_on=datetime.now())
            db.session.add(user)
            db.session.commit()
            return make_response({'message': 'User Added'}), HTTPStatus.CREATED
    except BaseException as e:
        return make_response({'message': 'Internal Server Error'}), HTTPStatus.BAD_REQUEST


def reset():
    try:
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        user = User.query.filter_by(username=username).first()

        if user:  # checks if user present or not
            if password != confirm_password:  # checks if confirm password valid
                return make_response({'message': 'Password Does not Match'}), HTTPStatus.BAD_REQUEST
            else:
                if check_password_hash(user.password, password):  # checks if password already been used
                    return make_response({'message': 'Password already been used.'}), HTTPStatus.CREATED
                else:  # valid scenario
                    User.query.filter_by(username=username).update(dict(password=generate_password_hash(password)))
                    db.session.commit()
                    return make_response({'message': 'Password Updated Successfully'}), HTTPStatus.CREATED
        else:
            return make_response({'message': 'User not registered'}), HTTPStatus.OK
    except Exception as e:
        return make_response({'message': 'Internal Server Error'}), HTTPStatus.BAD_REQUEST
