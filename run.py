from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # db init
    db.init_app(app)

    # creates blueprint for app to be used across thew project
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from routes import route as route_blueprint
    app.register_blueprint(route_blueprint)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port="8085", debug=True) # starting the app
