INSERT INTO users (username, password, name) VALUES
('alice123', '12345678', 'Alice Johnson'),
('bob456', '12345678', 'Bob Smith'),
('charlie789', '12345678', 'Charlie Brown');

INSERT INTO income (user_id, amount, income_date, description) VALUES
(5, 5000.00, '2025-05-01', 'Monthly salary'),
(2, 200.00, '2025-05-03', 'Freelance logo design'),
(3, 1500.00, '2025-05-05', 'Academic scholarship');

INSERT INTO expenses (user_id, amount, category, expense_date, description) VALUES
(4, 120.50, 'Groceries', '2025-05-06', 'Weekly groceries'),
(4, 50.00, 'Transport', '2025-05-07', 'Taxi ride'),
(2, 300.00, 'Electronics', '2025-05-04', 'Bought headphones'),
(3, 25.00, 'Books', '2025-05-08', 'Textbooks');

INSERT INTO budget (user_id, category, budget_limit, start_date, end_date) VALUES
(2, 'Groceries', 500.00, '2025-05-01', '2025-05-31'),
(2, 'Electronics', 400.00, '2025-05-01', '2025-05-31'),
(3, 'Books', 100.00, '2025-05-01', '2025-05-31');

INSERT INTO savings_goals (user_id, goal_name, target_amount, saved_amount, deadline) VALUES
(2, 'New Laptop', 1000.00, 300.00, '2025-12-31'),
(2, 'Vacation', 2000.00, 500.00, '2025-08-01'),
(3, 'Emergency Fund', 500.00, 100.00, '2025-06-30');

INSERT INTO categories (user_id, category_name, type) VALUES
(2, 'Groceries', 'expense'),
(2, 'Salary', 'income'),
(2, 'Freelance', 'income'),
(3, 'Books', 'expense'),
(3, 'Scholarship', 'income');

