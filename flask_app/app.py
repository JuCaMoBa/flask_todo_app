from flask import Flask
from flask_app.blueprints.auth_blueprint.auth_blueprint import  auth_bp
from flask_app.blueprints.task_blueprint.task_blueprint import  task_bp
from flask_app.blueprints.home_blueprint.home_blueprint import  home_bp

app = Flask(__name__)


# Registrar los Blueprints
app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(task_bp)


# Agregar la secret key
app.config['SECRET_KEY'] = 'tu_clave_secreta'


