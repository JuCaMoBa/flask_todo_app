from flask import Blueprint, request

from flask_app.utils.login_required import login_required

task_bp = Blueprint(
    'tasks', 
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/tasks'
)

@task_bp.before_request
def before_request():
    return login_required()


from . import task_routes

