from flask import Flask
from flask_login import LoginManager
from services.models import User
from services import user_service


app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_bp.login' 


@login_manager.user_loader
def load_user(user_id):
    conn = user_service.get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users_auth WHERE id = %s", (user_id,))
    user = cur.fetchone()
    conn.close()

    if user:
        return User(id=user[0], name=user[1], email=user[2], password=user[3])
    return None




# Agregar la secret key
app.config['SECRET_KEY'] = 'tu_clave_secreta'

