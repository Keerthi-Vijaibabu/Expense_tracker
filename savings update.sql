DELIMITER //

CREATE PROCEDURE calculate_monthly_savings(
    IN input_user_id INT,
    IN input_year INT,
    IN input_month INT
)
BEGIN
    DECLARE total_income DECIMAL(10,2);
    DECLARE total_expense DECIMAL(10,2);
    DECLARE net_savings DECIMAL(10,2);

    SELECT IFNULL(SUM(amount), 0)
    INTO total_income
    FROM income
    WHERE user_id = input_user_id
      AND YEAR(date) = input_year
      AND MONTH(date) = input_month;

    SELECT IFNULL(SUM(amount), 0)
    INTO total_expense
    FROM expenses
    WHERE user_id = input_user_id
      AND YEAR(date) = input_year
      AND MONTH(date) = input_month;

    SET net_savings = total_income - total_expense;

    INSERT INTO savings (user_id, year, month, amount_saved)
    VALUES (input_user_id, input_year, input_month, net_savings);
END //

DELIMITER ;

