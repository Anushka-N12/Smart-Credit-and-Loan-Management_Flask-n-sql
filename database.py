import mysql.connector

def get_db_connection():
    db = mysql.connector.connect(
        host='localhost',
        user='b2635299',
        password='Cab#22se',
        database='b2635299',
        auth_plugin='mysql_native_password',
    )
    return db