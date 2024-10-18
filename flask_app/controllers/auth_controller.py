from flask import flash, redirect, render_template, request, session, url_for
from services.auth_service import AuthService
from repositories.user_respository import UserRepository
from database.db_connection import DatabaseConnection


db_connection = DatabaseConnection()
user_repository = UserRepository(db_connection)

auth_service = AuthService(user_repository)

def login():
    credentials = {
        'email': request.form['email'],
        'password': request.form['password']
    }

    user = auth_service.check_credentials(credentials)

    if user:
        session['user'] = user
        return redirect(url_for('tasks.profile'))  
    flash('Por favor verifica tus credenciales')

    return redirect(url_for('auth.login'))

def login_render_form():
    return render_template('login.html')

def signup():
    credentials = {
        'name': request.form['name'],
        'email': request.form['email'],
        'password': request.form['password']
    }
   
    existing_user = auth_service.check_email(credentials)

    if existing_user:
        # Si el correo ya está registrado, mostrar un mensaje y renderizar la página de signup
        flash('El email ya está registrado. Por favor, intente con otro o diríjase a la pagina de login', 'error')
        return redirect(url_for('auth.signup'))
    else: 
        auth_service.create_user(**credentials)
        flash('Te has registrado exitosamente, inicia sesión con tus credenciales ', 'success')
        return redirect(url_for('auth.login'))
    
def signup_render_form():
    return render_template('signup.html')

def logout():
    del session['user']
    return redirect(url_for('auth.login'))