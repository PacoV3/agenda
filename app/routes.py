from flask import render_template, flash, redirect, url_for
from app import app, db, Bootstrap
from app.forms import LoginForm, ContactForm, SignUpForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Contact
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    # Si no ha entrado el usuario
    if not current_user.is_authenticated:
        # Mandalo al Login
        return redirect(url_for('login'))
    # De otra forma carga el index
    contactos = Contact.query.filter_by(users_id=current_user.id).all()
    return render_template('index.html', title="Contactos", contactos=contactos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Si el usuario ya ingreso mandalo al index
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    # Si hace un submit
    if form.validate_on_submit():
        # Haz una consulta de usuarios con el mismo nombre
        user = User.query.filter_by(username=form.username.data).first()
        # Si no se encontro el usuario o la contraseña es incorrecta
        if user is None or not user.check_password(form.password.data):
            # Muestra el error
            flash('No se encontro el usuario o la contraseña es incorrecta')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash('Iniciaste sesión correctamente, Hola {}'.format(form.username.data))
        return redirect('/index')
    return render_template('login.html', title='Login', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # Si el usuario ya ingreso mandalo al index
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignUpForm()
    # Si hace un submit
    if form.validate_on_submit():
        # Haz una consulta de usuarios con el mismo nombre
        check_username = User.query.filter_by(username=form.username.data).first()
        if check_username:
            # Muestra el error
            flash('Nombre de usuario ya existente.')
            return redirect(url_for('signup'))
        # Validar correo
        check_username = User.query.filter_by(email=form.email.data).first()
        if check_username:
            # Muestra el error
            flash('Correo ya existente.')
            return redirect(url_for('signup'))
        user = User()
        user.username = form.username.data
        user.email = form.email.data
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', title='Registro', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/contact', methods=['GET', 'POST'])
@login_required
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        nuevo_contacto = Contact()
        # El contacto es lo que se recibe del form
        nuevo_contacto.nombre = form.nombre.data
        nuevo_contacto.telefono = form.telefono.data
        nuevo_contacto.email = form.email.data
        # El id es el id del objeto usuario actual
        nuevo_contacto.users_id = current_user.id
        # Añadir y enviar a la bd
        db.session.add(nuevo_contacto)
        db.session.commit()
        return redirect(url_for('index'))
    # Si es POST insertar el contacto
    return render_template('contact.html', title='Añadir Contacto', form=form)

@app.route('/contact/delete/<int:id>', methods=['POST'])
@login_required
def delete_contact(id):
    contact = Contact.query.filter_by(id=id).first()
    if contact:
        if current_user.id == contact.users_id:
            db.session.delete(contact)
            db.session.commit()
        else:
            flash("No tienes permisos para borrar este contacto")
    else:
        flash("El contacto no existe")
    return redirect(url_for('index'))
    
@app.route('/contact/edit/<int:id>', methods=['POST'])
@login_required
def edit_contact(id):
    contact = Contact.query.filter_by(id=id).first()
    if contact:
        if current_user.id == contact.users_id:
            form = ContactForm()
            if form.validate_on_submit():
                contact.nombre = form.nombre.data
                contact.telefono = form.telefono.data
                contact.email = form.email.data
                db.session.add(contact)
                db.session.commit()
                return redirect(url_for('index'))
            form.nombre.data = contact.nombre 
            form.telefono.data = contact.telefono 
            form.email.data = contact.email
            return render_template('contact.html', form=form, edit=True)
        else:
            flash("No tienes permisos para cambiar este contacto")
    else:
        flash("El contacto no existe")
    return redirect(url_for('index'))
