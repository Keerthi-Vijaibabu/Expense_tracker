# Expense_tracker
# 💰 Expense_Tracker

A simple web-based expense tracking application built using Flask. It allows users to register, login, and track their income and expenses. It also includes dynamic dashboard views and basic validations.

---

## 🛠 Features

- 📝 User Registration and Login
- 📥 Add and View Income
- 💸 Add and View Expenses
- 📊 Dashboard for Visual Summary
- ✅ Front-end Form Validation
- ⚙️ SQL Integration
- 🔐 Session-based Authentication

---

## 🧱 Project Structure
expense_tracker/
│
├── app.py # Main application file
├── db.py # DB connection helper
├── new_user_trigger.sql # SQL triggers for new users
├── assets/ # Static assets like icons
│ └── favicon.svg
├── static/
│ ├── css/
│ │ └── styles.css
│ └── js/
│ ├── validation.js
│ ├── theme.js
│ └── sidebar.js
├── templates/
│ ├── index.html
│ ├── register.html
│ ├── register1.html
│ ├── dashboard.html
│ ├── income.html
│ └── expense.html
└── .gitignore


---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.10+ installed and virtual environment enabled.

### 1. Clone the Repository
git clone https://github.com/Keerthi-Vijaibabu/expense_tracker.git
cd expense_tracker

### 2. Create and Activate Virtual Environment

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
### 3. Install Dependencies

pip install -r requirements.txt

(Note: Create requirements.txt using pip freeze > requirements.txt)

4. Run the App

python app.py
Visit http://127.0.0.1:5000/ in your browser.

