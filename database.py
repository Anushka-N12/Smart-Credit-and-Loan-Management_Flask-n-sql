import mysql.connector

def get_db_connection():
    db = mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='your_database',
        auth_plugin='mysql_native_password',
    )
    return db