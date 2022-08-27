from flask_sqlalchemy import SQLAlchemy 
from ..app import app

db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))