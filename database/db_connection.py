import os
import psycopg2


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user=os.environ['DB_USER'],
                            password=os.environ['DB_PASSWORD'])
    return conn
   

