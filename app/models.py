from app import db, app
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from flask_login import UserMixin
import os

class Users(UserMixin, db.Model):
    ID_User = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(64), index=True, unique=True)
    Givenname = db.Column(db.String(64))
    Surname = db.Column(db.String(64))
    Mail = db.Column(db.String(128), index=True, unique=True)
    Password = db.Column(db.String(128))
    ToDos = db.relationship('ToDos', backref='User_ID', lazy='dynamic')
    Comments = db.relationship('Comments', backref='ToDo_ID', lazy='dynamic')

class ToDos(db.Model):
    ID_ToDo = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64))
    Description = db.Column(db.String(128))
    Status = db.Column(db.String(16))
    Date = db.Column(db.DateTime, default=datetime.utcnow)
    User_ID = db.Column(db.Integer, db.ForeignKey(Users.ID_User))

class Comments(db.Model):
    ID_Comment = db.Column(db.Integer, primary_key=True)
    Titel = db.Column(db.String(64))
    Content = db.Column(db.String(256))
    Timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    User_ID = db.Column(db.Integer, db.ForeignKey(Users.ID_User))
    ToDo_ID = db.Column(db.Integer, db.ForeignKey(ToDos.ID_ToDo))