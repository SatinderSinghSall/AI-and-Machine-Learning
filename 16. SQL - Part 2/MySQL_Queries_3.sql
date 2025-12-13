SHOW DATABASES;

USE ECommerce;
SHOW TABLES;
SELECT * FROM Custommers;
SELECT * FROM Orders;

-- Sub-Queries in SQL:
SELECT * FROM Orders
WHERE Amount > (
	SELECT AVG(Amount)
    FROM Orders
);
