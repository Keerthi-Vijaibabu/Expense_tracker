delimiter $$

CREATE TRIGGER new_user
AFTER INSERT ON users
FOR EACH ROW

BEGIN
	
	INSERT into income (user_id, amount, income_date, description)
    values (NEW.user_id, 0, NEW.registration_date, 'new user');
   
END;
$$
Delimiter ;
