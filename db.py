import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Keerthi@12",
        database="expense",
        port = 3307
    )
