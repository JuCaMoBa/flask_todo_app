from flask_app.app import app
from flask_app.controller import auth_bp


# Registrar los Blueprints
app.register_blueprint(auth_bp)


