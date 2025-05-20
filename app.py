from flask import Flask, render_template, request, redirect, session
from db import get_db
from datetime import date, datetime

now = datetime.now()

app = Flask(__name__)
app.secret_key = 'f9a8f7c3c9e14b8a3fa5dc092bfea3b2a4ccdef26d27fae1dc82a9db9c14fd21'

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT user_id, password FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        cursor.close()
        db.close()

        if result and password == result[1]:
            session['user'] = result[0]
            return redirect('/')
        else:
            error = 'Invalid username or password'

    return render_template('index.html', error=error)

# Register Route
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
            try:
                db = get_db()
                cursor = db.cursor()
                cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
                if cursor.fetchone():
                    error = "Username already exists"
                else:
                    cursor2 = db.cursor()
                    cursor2.execute(
                        "INSERT INTO users (username, password, name) VALUES (%s, %s, %s)",
                        (username, password, full_name)
                    )
                    cursor2.close()
                    db.commit()

                    # Auto-login after register
                    cursor2 = db.cursor()
                    cursor2.execute("SELECT user_id FROM users WHERE username = %s", (username,))
                    user_id = cursor2.fetchone()[0]
                    session['user'] = user_id
                    cursor2.close()
                    cursor.close()
                    db.close()
                    return redirect('/')
                cursor.close()
                db.close()
            except Exception as e:
                error = f"Database error: {e}"

    return render_template('register.html', error=error)

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

# Dashboard Route
@app.route('/')
# Savings should be changed and recalculated
def dashboard():
    if 'user' not in session:
        return redirect('/login')

    db = get_db()
    total_exp = 0
    income_val = 0
    cursor = db.cursor()
    cursor.execute("SELECT * FROM expenses WHERE user_id = %s", (session.get('user'),))
    expenses = cursor.fetchall()
    total_exp = sum([e[2] for e in expenses]) if expenses else 0
    expenses = expenses if expenses else None
    expenses = expenses[::-1]
    cursor.close()

    cursor = db.cursor()
    cursor.execute("SELECT amount FROM income WHERE user_id = %s", (session.get('user'),))
    income = cursor.fetchall()
    cursor.close()
    income_val = sum([i[0] for i in income]) if expenses else 0
    balance = income_val - total_exp if income_val else None

    cursor = db.cursor()
    cursor.execute("SELECT name, username FROM users WHERE user_id = %s;", (session.get('user'),))
    l = cursor.fetchone()
    name = l[0]
    username = l[1]


    savings = 0
    if now.day == 30:
        cursor = db.cursor()
        cursor.execute("calculate_monthly_savings();")
        cursor.close()

    cursor = db.cursor()
    cursor.execute("SELECT amount_saved FROM savings WHERE user_id = %s", (session.get('user'),))
    saving = cursor.fetchall()
    for i in saving:
        print(i)
    savings = sum([s[2] for s in saving]) if saving else 0

    return render_template('dashboard.html', name = name, username = username, total=total_exp, expenses=expenses, income=income_val, balance=balance, savings = savings)

# View Expenses
@app.route('/expenses')
def view_expenses():
    if 'user' not in session:
        return redirect('/login')

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM expenses WHERE user_id = %s", (session.get('user'),))
    expenses = cursor.fetchall()
    cursor.close()
    db.close()

    return render_template('expense.html', expenses=expenses)

# Add Expense
@app.route('/add_exp', methods=['POST'])
def add_expense():
    if 'user' not in session:
        return redirect('/login')

    amount = request.form.get('amount')
    category = request.form.get('category')
    description = request.form.get('description')
    today = date.today()

    db = get_db()
    cursor = db.cursor()
    sql = "INSERT INTO expenses (user_id, amount, category, expense_date, description) VALUES (%s, %s, %s, %s, %s)"
    val = (session.get('user'), amount, category, today, description)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()

    return redirect('/')

#Add Income
@app.route('/add_inc', methods=['POST'])
def add_income():
    if 'user' not in session:
        return redirect('/login')

    # Get and validate form data
    try:
        amount = float(request.form.get('amount'))  # Convert to float for numeric safety
        date = request.form.get('date')
        category = request.form.get('category')
        description = request.form.get('description')

        if not (amount and date and category):  # Basic validation
            return "Missing required fields", 400

        db = get_db()
        cursor = db.cursor()

        sql = """
            INSERT INTO income (user_id, amount, income_date, description)
            VALUES (%s, %s, %s, %s)
        """
        val = (session.get('user'), amount, date, description)
        cursor.execute(sql, val)
        db.commit()

    except Exception as e:
        db.rollback()
        return f"Error adding income: {str(e)}", 500

    finally:
        cursor.close()
        db.close()

    return redirect('/')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
