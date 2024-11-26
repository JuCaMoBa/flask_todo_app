import os
import psycopg2
import psycopg2.extras


db_config = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_DATABASE'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'port': os.getenv('PORT_DB')
}
class DatabaseConnection():
    def __enter__(self):
        self.conn = psycopg2.connect(**db_config)
        self.cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
                        
        self.cursor.close()
        self.conn.close()



   

