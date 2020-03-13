from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.config import Config

app = Flask(__name__)

config = Config
from app.framework.config import *
Configurate(app, Config)
db =  SQLAlchemy(app)
migrate = Migrate(app, db)
from app import http, framework, kernel, model
from app.framework.util.template import ViewFunction
ViewFunction(app)