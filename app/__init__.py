from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from app.config import Config
from app.framework.util.locale.localization import *

app = Flask(__name__)
CORS(app)
config = Config

from app.framework.config import *

Configurate(app, Config)


db =  SQLAlchemy(app)
login = LoginManager(app)
migrate = Migrate(app, db)

login.login_view = "UserController:login_view"

from app import http, framework, kernel, model
from app.framework.util.template import ViewFunction

ViewFunction(app)

