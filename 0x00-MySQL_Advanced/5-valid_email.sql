-- Task 5: Email validation trigger - This trigger resets the valid_email attribute
-- only if the email has been modified.
DELIMITER |
CREATE TRIGGER email_bool BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = FALSE;
    END IF;
END;
