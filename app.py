from flask import Flask, render_template, request, redirect, session
from db import cursor
app = Flask(__name__)
# Add secret key for session
app.secret_key = 'f9a8f7c3c9e14b8a3fa5dc092bfea3b2a4ccdef26d27fae1dc82a9db9c14fd21'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        query = "Select password from users where username =", username
        cursor.execute(query)
        password_correct = cursor.fetchone
        if password == password_correct:
            session['user'] = username
            return redirect('/')
        else:
            error = 'Invalid username or password'

    return render_template('login.html', error=error)

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

# Home Route (view all expenses)
@app.route('/')
def index():
    if 'user' not in session:
        return redirect('/login')
    
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    return render_template('index.html', expenses=expenses)

# Add Expense Route
@app.route('/add', methods=['POST'])
def add_expense():
    if 'user' not in session:
        return redirect('/login')
    
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
