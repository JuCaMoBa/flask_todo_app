from .home_blueprint import home_bp
from flask_app.controllers.home_controller import home

home_bp.add_url_rule(
    '/',
    view_func=home,
    methods = ['GET']
)