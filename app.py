from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="your_mysql_username",
    password="your_mysql_password",
    database="expense_db"
)
cursor = db.cursor()

# Home Route (view all expenses)
@app.route('/')
def index():
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    return render_template('index.html', expenses=expenses)

# Add Expense Route (handle form submission)
@app.route('/add', methods=['POST'])
def add_expense():
    amount = request.form['amount']
    category = request.form['category']
    description = request.form['description']

    sql = "INSERT INTO expenses (amount, category, description) VALUES (%s, %s, %s)"
    val = (amount, category, description)
    cursor.execute(sql, val)
    db.commit()

    return redirect('/')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
