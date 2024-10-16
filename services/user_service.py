from flask import flash, redirect, url_for
from database.db_connection import get_db_connection

class UserService():

    def insert_user(self, name, email, password):
        with get_db_connection() as cursor:
            cursor.execute('INSERT INTO users_auth (name, email, password)'
                        'VALUES (%s, %s, %s)',
                        (name, email, password)) 

    def check_user(self, credentials):
        with get_db_connection() as cursor:
            cursor.execute('SELECT id, name, email, password FROM users_auth WHERE email = %(email)s', credentials)
            return cursor.fetchone()
        
    def check_email(self, email):
        with get_db_connection() as cursor:
            cursor.execute('SELECT id, name, email, password  FROM users_auth WHERE email = %(email)s', email)
            return cursor.fetchone()
        
    def read_tasks (self, id):
        with get_db_connection() as cursor:
            cursor.execute('SELECT * FROM tasks WHERE user_id = %s', (id,))
            return cursor.fetchall()
        
    def insert_task (self, user_id, task_description):
        with get_db_connection() as cursor:
            cursor.execute('INSERT INTO tasks (user_id, task_description)'
                            'VALUES (%s, %s)',
                            (user_id, task_description)
                            )

    def delete_task(self, task_id):
        with get_db_connection() as cursor:
            cursor.execute('DELETE FROM tasks WHERE task_id = %s', (task_id,))


    def update_task(self, task_description, task_status, task_id):
        with get_db_connection() as cursor:
            cursor.execute("UPDATE tasks SET task_description = %s,task_status = %s WHERE task_id = %s;", (task_description, task_status, task_id))


        

    


        



