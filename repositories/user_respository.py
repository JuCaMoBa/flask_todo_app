from database.db_connection import DatabaseConnection


class UserRepository:
       
        def __init__(self, db: DatabaseConnection):
           self.db = db
          
        def insert_user(self, name, email, password):
            with self.db as cursor:
                cursor.execute('INSERT INTO users_auth (name, email, password)'
                        'VALUES (%s, %s, %s)',
                        (name, email, password)) 
                
        def select_user(self,credentials):
            with self.db as cursor:
                cursor.execute('SELECT id, name, email, password FROM users_auth WHERE email = %(email)s', credentials)
                return cursor.fetchone()