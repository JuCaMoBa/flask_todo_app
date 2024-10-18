from flask import Blueprint

from flask_app.controllers.home_controller import home

home_bp = Blueprint('home', 
                    __name__,
                    template_folder='templates',
                    static_folder='static')

home_bp.add_url_rule(
    '/',
    view_func=home,
    methods = ['GET']
)