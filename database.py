import mysql.connector

def get_db_connection():
    db = mysql.connector.connect(
        host='localhost',
        user='________',          #Filled in locally
        password='________',
        database='________',
        auth_plugin='mysql_native_password',
    )
    return db
