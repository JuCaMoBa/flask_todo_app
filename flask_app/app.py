from flask import Flask
from flask_login import LoginManager
from services.models import User
from database.db_connection import get_db_connection


app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_bp.login' 


@login_manager.user_loader
def load_user(user_id):
    with get_db_connection() as cursor:
        cursor.execute("SELECT * FROM users_auth WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        if user:
            return User(id=user['id'], name=user['name'], email=user['email'], password=user['password'])
        return None




# Agregar la secret key
app.config['SECRET_KEY'] = 'tu_clave_secreta'

