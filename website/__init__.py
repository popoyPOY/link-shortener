from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import random
import string

db = SQLAlchemy()

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'development'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from . import models 
    
    with app.app_context():
     db.create_all()

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("Success")



def random_str():
   letters = string.ascii_lowercase
   result = ''.join(random.choice(letters) for i in range(10))

   return result