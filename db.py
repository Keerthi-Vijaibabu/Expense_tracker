import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="sivasubhi2468",
        database="expense",
        port = 3306
    )
