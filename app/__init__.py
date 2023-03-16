# Übernommen aus den Beispielen
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from config import Config

# Übernommen aus den Beispielen
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

# Übernommen aus den Beispielen
bootstrap = Bootstrap(app)

from app import routes, models, api