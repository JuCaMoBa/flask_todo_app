from flask import Blueprint, redirect, request, session, url_for

auth_bp = Blueprint('auth', 
                    __name__,
                    template_folder='templates',
                    static_folder='static')

@auth_bp.before_request
def user_is_logged_in():
    if request.endpoint in ['auth.login_render_form', 'auth.signup_render_form'] and session.get('user', False):
        return redirect(url_for('tasks.view_tasks'))

from . import auth_routes