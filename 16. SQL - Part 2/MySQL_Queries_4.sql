-- =====================================================
-- SQL VIEWS, INDEXES, COMPOSITE INDEXES & PROCEDURES
-- Database: ECommerce
-- =====================================================

USE ECommerce;

-- =====================================================
-- 1. VIEWS IN SQL
-- A view is a virtual table based on a SELECT query
-- =====================================================

-- Create a simple view
CREATE VIEW view_customers_mumbai AS
SELECT customer_id, name, city
FROM customers
WHERE city = 'Mumbai';

-- View data from view
SELECT * FROM view_customers_mumbai;

-- Create view using JOIN
CREATE VIEW view_customer_orders AS
SELECT c.customer_id, c.name, o.order_id, o.amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;

SELECT * FROM view_customer_orders;

-- Drop a view
DROP VIEW IF EXISTS view_customers_mumbai;

-- =====================================================
-- 2. INDEX IN SQL
-- Index improves SELECT query performance
-- =====================================================

-- Create an index on city column
CREATE INDEX idx_customers_city
ON customers(city);

-- Use index implicitly
SELECT * FROM customers WHERE city = 'Delhi';

-- Drop index
DROP INDEX idx_customers_city ON customers;

-- =====================================================
-- 3. COMPOSITE INDEX
-- Index on multiple columns
-- =====================================================

-- Create composite index
CREATE INDEX idx_orders_customer_amount
ON orders(customer_id, amount);

-- Query using composite index
SELECT * FROM orders
WHERE customer_id = 1 AND amount > 500;

-- Drop composite index
DROP INDEX idx_orders_customer_amount ON orders;

-- =====================================================
-- 4. STORED PROCEDURES
-- A stored procedure is a reusable SQL block
-- =====================================================

DELIMITER $$

-- Procedure to get orders by customer id
CREATE PROCEDURE GetOrdersByCustomer(IN cust_id INT)
BEGIN
    SELECT * FROM orders
    WHERE customer_id = cust_id;
END $$

DELIMITER ;

-- Call procedure
CALL GetOrdersByCustomer(1);

-- =====================================================
-- 5. PROCEDURE WITH INSERT
-- =====================================================

DELIMITER $$

CREATE PROCEDURE AddOrder(
    IN o_id INT,
    IN c_id INT,
    IN amt INT
)
BEGIN
    INSERT INTO orders VALUES (o_id, c_id, amt);
END $$

DELIMITER ;

-- Call insert procedure
CALL AddOrder(105, 3, 800);

-- =====================================================
-- 6. DROP PROCEDURE
-- =====================================================

DROP PROCEDURE IF EXISTS GetOrdersByCustomer;
DROP PROCEDURE IF EXISTS AddOrder;
