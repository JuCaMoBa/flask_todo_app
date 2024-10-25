from flask import flash, redirect, render_template, request, session, url_for
from services.task_service import TaskService
from repositories.task_repository import TaskRepository
from database.db_connection import DatabaseConnection


db_connection = DatabaseConnection()
task_repository = TaskRepository(db_connection)

task_service = TaskService(task_repository)


def view_tasks():

    result = task_service.read_tasks(session['user']['id'])
    tasks = [dict(row.items()) for row in result]

    id = session['user']['id']

    return render_template('tasks.html', name = session['user']['name'], tasks= tasks)

def create_task():
    task_description = request.form.get('task_description')

    id = session['user']['id']
    
    task_service.create_task(id, task_description)
           
    return redirect(url_for('tasks.view_tasks'))

def delete_task(task_id):
    task_service.delete_task(task_id)
           
    return redirect(url_for('tasks.view_tasks'))

def update_task(task_id):
    task_description = request.form.get('task_description')
    task_status = request.form.get('task_status')

    task_service.update_task(task_description,task_status, task_id)

    return redirect(url_for('tasks.view_tasks'))