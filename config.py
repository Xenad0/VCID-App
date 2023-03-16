# Übernommen aus den Beispielen
import os

# Übernommen aus den Beispielen
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECURITY_KEY_FORMS'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')