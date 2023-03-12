import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECURITY_KEY_FORMS'
    SERVER_NAME='wa-todo-prod-02aaf488.azurewebsites.net:443'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')