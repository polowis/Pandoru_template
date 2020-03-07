from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.config import Config

app = Flask(__name__)
config = Config
from app.framework.config import *
Configurate(app, Config)

from app import http, framework, kernel