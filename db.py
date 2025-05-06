import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Keerthi@12",
    port = 3307,
    database="expense"
)

cursor = db.cursor()