
create database expense;

use expense;

CREATE TABLE expenses (
    expense_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    amount DECIMAL(10, 2),
    category VARCHAR(50),
    expense_date DATE,
    description VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255),
    name VARCHAR(100),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE income (
    income_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    amount DECIMAL(10, 2),
    category VARCHAR(50),
    income_date DATE,
    description VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE budget (
    budget_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    category VARCHAR(50),
    budget_limit DECIMAL(10, 2),
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE savings_goals (
    goal_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    goal_name VARCHAR(100),
    target_amount DECIMAL(10, 2),
    saved_amount DECIMAL(10, 2) DEFAULT 0,
    deadline DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    category_name VARCHAR(50),
    type ENUM('income', 'expense'),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);