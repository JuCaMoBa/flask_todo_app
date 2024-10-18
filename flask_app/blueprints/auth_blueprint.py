from flask import Blueprint

from flask_app.controllers.auth_controller import login, login_render_form, logout, signup, signup_render_form


auth_bp = Blueprint('auth', 
                    __name__,
                    template_folder='templates',
                    static_folder='static')

auth_bp.add_url_rule(
    '/login',
    view_func=login,
    methods = ['POST']
)

auth_bp.add_url_rule(
    '/login',
    view_func=login_render_form,
    methods = ['GET']
)

auth_bp.add_url_rule(
    '/register',
    view_func=signup,
    methods = ['POST']
)

auth_bp.add_url_rule(
    '/register',
    view_func=signup_render_form,
    methods = ['GET']
)

auth_bp.add_url_rule(
    '/logout',
    view_func=logout,
    methods = ['GET']
)