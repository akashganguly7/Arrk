from auth import *
route = Blueprint('route', __name__)

#manage routing here
route.add_url_rule('/login', methods=['POST'],view_func=login)
route.add_url_rule('/signup', methods=['POST'],view_func=signup)
route.add_url_rule('/reset', methods=['POST'],view_func=reset)
