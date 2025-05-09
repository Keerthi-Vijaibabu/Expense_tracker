from flask import Flask, render_template, request, redirect, session
from db import cursor, db
from datetime import date

app = Flask(__name__)
# Add secret key for session
app.secret_key = 'f9a8f7c3c9e14b8a3fa5dc092bfea3b2a4ccdef26d27fae1dc82a9db9c14fd21'

#Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute("SELECT user_id, password FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()

        if result and password == result[1]:
            session['user'] = result[0]
            return redirect('/')
        else:
            error = 'Invalid username or password'

    return render_template('index.html', error=error)

#Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        full_name = request.form.get('name', '').strip()
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        confirm = request.form.get('confirmPassword', '').strip()

        if password != confirm:
            error = "Passwords do not match"
        else:
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            existing_user = cursor.fetchone()
            cursor.close()
            if existing_user:
                error = "Username already exists"
            else:
                try:
                    cursor.execute(
                        "INSERT INTO users (username, password, name) VALUES (%s, %s, %s)",
                        (username, password, full_name)
                    )
                    db.commit()
                    return redirect('/login')
                except Exception as e:
                    db.rollback()  # Optional safety
                    error = f"DB error: {e}"

    return render_template('register.html', error=error)

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')


# Dashboard (view all expenses)
@app.route('/')
def dashboard():
    if 'user' not in session:
        return redirect('/login')

    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    total_exp = 0
    if len(cursor) != 0:
        for i in expenses:
            total_exp += i[1]

    cursor.execute("SELECT amount FROM income WHERE user_id = %s", (session.get('user'),))
    income = cursor.fetchone()
    query = "SELECT amount from income where user_id == " + session.get('user')
    return render_template('dashboard.html', total=total_exp, expenses=expenses, income=income, savings=None)


#Expenses
@app.route('/add')
def expenses():
    if 'user' not in session:
        return redirect('/login')

    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    total_exp = 0
    if len(cursor) != 0:
        for i in expenses:
            total_exp += i[1]

    return render_template('index.html', expenses=expenses)

# Add Expense Route
@app.route('/add', methods=['POST'])
def add_expense():
    if 'user' not in session:
        return redirect('/login')

    amount = request.form['amount']
    category = request.form['category']
    description = request.form['description']
    today = date.today()

    sql = "INSERT INTO expenses (user_id, amount, category, expense_date, description) VALUES (%s, %s, %s, %s, %s)"
    val = (session.get('user'), amount, category, today, description)
    cursor.execute(sql, val)
    db.commit()

    return redirect('/')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)