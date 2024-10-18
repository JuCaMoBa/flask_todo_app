from flask import Blueprint

from flask_app.controllers.task_controller import profile, profile_delete_task, profile_render_template, profile_update_task 


task_bp = Blueprint('tasks', 
                    __name__,
                    template_folder='templates',
                    static_folder='static')

task_bp.add_url_rule(
    '/profile',
    view_func=profile,
    methods = ['POST']
)

task_bp.add_url_rule(
    '/profile',
    view_func=profile_render_template,
    methods = ['GET']
)

task_bp.add_url_rule(
    '/profile/delete_task/<int:task_id>',
    view_func=profile_delete_task,
)

task_bp.add_url_rule(
    '/profile/update_task/<int:task_id>',
    view_func=profile_update_task,
    methods = ['POST']
)