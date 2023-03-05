from app import db, app
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from flask_login import UserMixin
from hashlib import md5

import os

class Users(UserMixin, db.Model):
    ID_User = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(64), index=True, unique=True)
    Givenname = db.Column(db.String(64))
    Surname = db.Column(db.String(64))
    Mail = db.Column(db.String(128), index=True, unique=True)
    Password = db.Column(db.String(128))
    ToDos = db.relationship('ToDos', backref='User', lazy='dynamic')
    Comments = db.relationship('Comments', backref='ToDo', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def get_id(self):
           return (self.ID_User)

    def set_password(self, password):
        self.Password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.Password, password)
    
    def avatar(self, size):
        digest = md5(self.Mail.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)
    
    def own_todos(self):
        todos = ToDos.query.filter_by(User_ID=self.ID_User)
        return todos.order_by(ToDos.Date.desc())
    
    def all_todos(self):
        todos = ToDos.query.all()
        return todos

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