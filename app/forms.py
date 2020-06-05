from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired('Campo obligatorio')])
    password = PasswordField("Contraseña", validators=[DataRequired('Campo obligatorio')])
    remember_me = BooleanField("Recuerdame")
    submit = SubmitField("Login")

class ContactForm(FlaskForm):
    nombre = StringField("Nombre del contacto", validators=[DataRequired('Campo obligatorio')])
    telefono = StringField("Teléfono")
    email = StringField("Correo")
    enviar_contacto = SubmitField("Añadir Contacto")

class SignUpForm(FlaskForm):
    username = StringField("Nombre de Usuario", validators=[DataRequired('Campo obligatorio')])
    email = StringField("Correo", validators=[DataRequired('Campo obligatorio')])
    password = StringField("Contraseña", validators=[DataRequired('Campo obligatorio')])
    signup = SubmitField("Registrar")
