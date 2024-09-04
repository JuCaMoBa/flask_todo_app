from flask import flash, redirect, render_template, request, url_for , Blueprint
from services.models import User
from services.user_service import UserService
from flask_login import login_user, login_required, current_user, logout_user


user_service = UserService()
auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    remember = True if request.form.get('remember') else False

    user_data = user_service.check_user(request.form)
    
    if not user_data:
        flash('Por favor verifica tu email y contraseña, los datos ingresados son incorrectos')
        return redirect(url_for('auth_bp.login'))
    
    user_obj = User(**user_data)
  
    login_user(user_obj, remember=remember)
    return redirect(url_for('auth_bp.profile')) 


@auth_bp.route('/login', methods=['GET'])
def login_render_form():
    return render_template('login.html')


@auth_bp.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    existing_user = user_service.check_email(request.form)

    if existing_user:
        # Si el correo ya está registrado, mostrar un mensaje y renderizar la página de signup
        flash('El email ya está registrado. Por favor, intente con otro o diríjase a la pagina de login', 'error')
        return redirect(url_for('auth_bp.signup'))
    else: 
        user_service.insert_user(name, email, password)
        return redirect(url_for('auth_bp.login'))


@auth_bp.route('/signup', methods=['GET'])
def signup_render_form():
    return render_template('signup.html')


@auth_bp.route('/profile', methods=['GET'])
@login_required
def profile_render_template():
    result = user_service.read_tasks(current_user.id)
    tasks = [dict(row.items()) for row in result]

    return render_template('profile.html', name = current_user.name, tasks= tasks)


@auth_bp.route('/profile', methods=['POST'])
@login_required
def profile():
    task_description = request.form.get('task_description')
    
    user_service.insert_task(current_user.id, task_description)
           
    return redirect(url_for('auth_bp.profile_render_template'))


@auth_bp.route('/profile/delete_task/<int:task_id>')
@login_required
def profile_delete_task(task_id):
    user_service.delete_task(task_id)
           
    return redirect(url_for('auth_bp.profile_render_template'))


@auth_bp.route('/profile/update_task/<int:task_id>', methods=['POST'])
@login_required
def profile_update_task(task_id):
    task_description = request.form.get('task_description')
    task_status = request.form.get('task_status')

    user_service.update_task(task_description,task_status, task_id)

    return redirect(url_for('auth_bp.profile_render_template'))


@auth_bp.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))



