from flask import Blueprint, request
from auth import *
route = Blueprint('route', __name__)

route.add_url_rule('/login', methods=['POST'],view_func=login)
route.add_url_rule('/signup', methods=['POST'],view_func=signup)
