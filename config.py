import os
import locale

basedir = os.path.abspath(os.path.dirname(__file__))

# Idioma "es-ES" (código para el español de España)
locale.setlocale(locale.LC_ALL, 'es-MX')

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "DASJE#$FGQP)5644F"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or \
        "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False