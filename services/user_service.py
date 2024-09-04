from flask import flash, redirect, url_for
from database.db_connection import get_db_connection
import psycopg2.extras




class UserService: 
    def __init__(self):
        self.conn = get_db_connection()
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    def close_connection(self):
        self.conn.close()

    def insert_user(self, name, email, password):
        self.cur.execute('INSERT INTO users_auth (name, email, password)'
                    'VALUES (%s, %s, %s)',
                    (name, email, password)) 

        self.conn.commit()

    def check_user(self, credentials):
        self.cur.execute('SELECT id, name, email, password FROM users_auth WHERE password = %(password)s and email = %(email)s', credentials)
        return self.cur.fetchone()
    
    def check_email(self, email):
        self.cur.execute('SELECT id, name, email, password  FROM users_auth WHERE email = %(email)s', email)
        return self.cur.fetchone()
    
    def read_tasks (self, id):
        self.cur.execute('SELECT * FROM tasks WHERE user_id = %s', (id,))
        return self.cur.fetchall()
    
    def insert_task (self, user_id, task_description):
        self.cur.execute('INSERT INTO tasks (user_id, task_description)'
                          'VALUES (%s, %s)',
                          (user_id, task_description)
                          )

        self.conn.commit()

    def delete_task(self, task_id):
        self.cur.execute('DELETE FROM tasks WHERE task_id = %s', (task_id,))

        self.conn.commit()

    def update_task(self, task_description, task_status, task_id):
        self.cur.execute("UPDATE tasks SET task_description = %s,task_status = %s WHERE task_id = %s;", (task_description, task_status, task_id))

        self.conn.commit()

        

    


        



