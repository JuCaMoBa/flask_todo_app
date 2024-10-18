from database.db_connection import DatabaseConnection


class TaskRepository:
            
        def __init__(self, db: DatabaseConnection):
           self.db = db
          
        def select_task(self,id):
            with self.db as cursor:
                cursor.execute('SELECT * FROM tasks WHERE user_id = %s', (id,))
                return cursor.fetchall()
                  
        def insert_task(self, user_id, task_description):
                with self.db as cursor:
                        cursor.execute('INSERT INTO tasks (user_id, task_description)'
                                'VALUES (%s, %s)',
                                (user_id, task_description)
                                )

        def delete_task(self, task_id):
                with self.db as cursor:
                        cursor.execute('DELETE FROM tasks WHERE task_id = %s', (task_id,))

        def update_task(self, task_description, task_status, task_id):
                with self.db as cursor:
                        cursor.execute("UPDATE tasks SET task_description = %s,task_status = %s WHERE task_id = %s;", (task_description, task_status, task_id))
            

