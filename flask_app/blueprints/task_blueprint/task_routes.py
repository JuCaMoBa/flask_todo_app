from  .task_blueprint import task_bp

from flask_app.controllers.task_controller import (
    create_task, 
    delete_task, 
    view_tasks, 
    update_task
) 

task_bp.add_url_rule(
    '/',
    view_func=create_task,
    methods = ['POST'],  
)

task_bp.add_url_rule(
    '/',
    view_func=view_tasks,
    methods = ['GET']
)

task_bp.add_url_rule(
    '/delete_task/<int:task_id>',
    view_func=delete_task,
)

task_bp.add_url_rule(
    '/update_task/<int:task_id>',
    view_func=update_task,
    methods = ['POST']
)