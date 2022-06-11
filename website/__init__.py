from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from apscheduler.schedulers.background import BackgroundScheduler
import concurrent.futures


# Initialize the database
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    # Create and configure an instance of the Flask application.
    app = Flask(__name__)

    # a default secret that should be overridden by instance config
    app.config['SECRET_KEY'] = "b'H\xe0_\xd4\xb5[\xf9\xd2\x15\x12\x0ciB\x94Aj\xb5\xdf\xae%H*\xda\xcf'"

    # store the database in the instance folder
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Servers

    create_database(app)

    return app


# Create database if db not exist
def create_database(app):
    if not path.exists(DB_NAME):
        db.create_all(app=app)
