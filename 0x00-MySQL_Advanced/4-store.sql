-- Task 4: Buy buy buy - This trigger reduces the quantity of an item when a new order is placed.
CREATE TRIGGER order_decrease BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
