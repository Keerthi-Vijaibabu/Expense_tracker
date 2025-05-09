import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sivasubhi2468",
    port = 3306,
    database="expense"
)

cursor = db.cursor()