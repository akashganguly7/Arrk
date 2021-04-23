from run import db

class User(db.Model):
    username = db.Column(db.String(128), primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    mobile = db.Column(db.String(255))
    created_on = db.Column(db.Date)
