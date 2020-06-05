# Se encarga de cargar las librerias
# Configurar las bases de datos, etc
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
Bootstrap(app)
login = LoginManager(app)
# Si no tiene permiso de entrar a algo mandalo al login
login.login_view = "login"

from app import routes, models
