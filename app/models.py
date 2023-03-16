# Übernommen aus den Beispielen
from app import db, app
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from flask_login import UserMixin
import base64
from hashlib import md5

import os

# Eigenentwicklung
class Users(UserMixin, db.Model):
    ID_User = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(64), index=True, unique=True)
    Givenname = db.Column(db.String(64))
    Surname = db.Column(db.String(64))
    Mail = db.Column(db.String(128), index=True, unique=True)
    Password = db.Column(db.String(128))
    API_Token = db.Column(db.String(32), unique=True)
    API_Expiration = db.Column(db.DateTime)
    ToDos = db.relationship('ToDos', backref='User', lazy='dynamic')
    Updates = db.relationship('Updates', backref='User2', lazy='dynamic')

    # Übernommen aus den Beispielen
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    # Eigenentwicklung
    def get_id(self):
           return (self.ID_User)

    # Übernommen aus den Beispielen
    def set_password(self, password):
        self.Password = generate_password_hash(password)

    # Übernommen aus den Beispielen
    def check_password(self, password):
        return check_password_hash(self.Password, password)
    
    # Übernommen aus den Beispielen
    def avatar(self, size):
        digest = md5(self.Mail.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)
    
    # Eigenentwicklung
    def own_todos(self):
        todos = ToDos.query.filter_by(User_ID=self.ID_User)
        return todos.order_by(ToDos.Date.desc())
    
    # Eigenentwicklung
    def all_todos(self):
        todos = ToDos.query.all()
        return todos
    
    # Eigenentwicklung
    def json_one(self):
        returndata = {
            'ID_User': self.ID_User,
            'Username': self.Username,
            'Givenname': self.Givenname,
            'Surname': self.Surname,
            'ToDos': self.ToDos.count(),
            'Updates': self.Updates.count()
        }

        return(returndata)

    # Übernommen aus den Beispielen
    def json_all():
        users = Users.query.all()
        returndata = {
            'users': [user.json_one() for user in users]
        }

        return(returndata)
    
    # Übernommen aus den Beispielen
    def get_token(self):
        now = datetime.utcnow()
        self.API_Token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.API_Expiration = now + timedelta(days=1)
        db.session.add(self)
        db.session.commit()
        return self.API_Token

    # Übernommen aus den Beispielen
    @staticmethod
    def check_token(token):
        user = Users.query.filter_by(API_Token=token).first()
        if user is None or user.API_Expiration < datetime.utcnow():
            return None
        return user

# Eigenentwicklung
class ToDos(db.Model):
    ID_ToDo = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64))
    Description = db.Column(db.String(1024))
    Status = db.Column(db.String(16))
    Date = db.Column(db.DateTime, default=datetime.utcnow)
    User_ID = db.Column(db.Integer, db.ForeignKey(Users.ID_User))

    # Eigenentwicklung
    def json_one(self):
        returndata = {
            'ID_ToDo': self.ID_ToDo,
            'Name': self.Name,
            'Description': self.Description,
            'Status': self.Status,
            'Date': self.Date,
            'User': self.User.Username
        }

        return(returndata)

    # Übernommen aus den Beispielen
    def json_all():
        todos = ToDos.query.all()
        returndata = {
            'todos': [todo.json_one() for todo in todos]
        }

        return(returndata)

# Eigenentwicklung
class Updates(db.Model):
    ID_Update = db.Column(db.Integer, primary_key=True)
    Titel = db.Column(db.String(64))
    Content = db.Column(db.String(256))
    Timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    User_ID = db.Column(db.Integer, db.ForeignKey(Users.ID_User))
    ToDo_ID = db.Column(db.Integer, db.ForeignKey(ToDos.ID_ToDo))

    # Eigenentwicklung
    def json_one(self):
        returndata = {
            'ID_Update': self.ID_Update,
            'Titel': self.Titel,
            'Content': self.Content,
            'Timestamp': self.Timestamp,
            'User': self.User2.Username,
            'ToDo_ID': self.ToDo_ID
        }

        return(returndata)

    # Übernommen aus den Beispielen
    def json_all():
        updates = Updates.query.all()
        returndata = {
            'updates': [update.json_one() for update in updates]
        }

        return(returndata)