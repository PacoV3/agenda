# Un modelo se asocia a una tabla de la base de datos
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db
from app import login
# UserMixin permite usar lo de las cookies
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"
    # Autoincremental con la llave primaria
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # backref es una referencia para atrás
    # lazy es como se cargan los datos
    # Es al nombre de la clase
    contactos = db.relationship("Contact", backref="owner", lazy = "dynamic")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User {}>".format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Contact(db.Model):
    __tablename__="contacts"
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(100), index=True)
    telefono = db.Column(db.String(18), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return "<Contact {}>".format(self.nombre)

# u = User()
# u.username = "Paco"
# u.email = "paco@gmail.com"
# u.set_password("Paco")
