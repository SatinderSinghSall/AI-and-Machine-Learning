-- =============================================
-- SQL SUBQUERIES : ALL EXAMPLES IN ONE FILE
-- Database: ECommerce
-- =============================================

-- Use database
USE ECommerce;

-- ---------------------------------------------
-- View Tables
-- ---------------------------------------------
SELECT * FROM customers;
SELECT * FROM orders;

-- =============================================
-- 1. SCALAR SUBQUERY (returns single value)
-- Orders with amount greater than average amount
-- =============================================
SELECT *
FROM orders
WHERE amount > (
    SELECT AVG(amount)
    FROM orders
);

-- =============================================
-- 2. SUBQUERY WITH IN
-- Customers who have placed at least one order
-- =============================================
SELECT *
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
);

-- =============================================
-- 3. SUBQUERY WITH NOT IN
-- Customers who have NOT placed any order
-- =============================================
SELECT *
FROM customers
WHERE customer_id NOT IN (
    SELECT customer_id
    FROM orders
);

-- =============================================
-- 4. SUBQUERY WITH EXISTS
-- Customers who have orders (using EXISTS)
-- =============================================
SELECT *
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);

-- =============================================
-- 5. CORRELATED SUBQUERY
-- Orders greater than the average order
-- of the same customer
-- =============================================
SELECT *
FROM orders o1
WHERE amount > (
    SELECT AVG(o2.amount)
    FROM orders o2
    WHERE o2.customer_id = o1.customer_id
);

-- =============================================
-- 6. SUBQUERY IN SELECT CLAUSE
-- Show customer name with total order amount
-- =============================================
SELECT 
    c.customer_id,
    c.name,
    (
        SELECT SUM(o.amount)
        FROM orders o
        WHERE o.customer_id = c.customer_id
    ) AS total_amount
FROM customers c;

-- =============================================
-- 7. SUBQUERY IN FROM CLAUSE (DERIVED TABLE)
-- Customers whose total purchase > 600
-- =============================================
SELECT *
FROM (
    SELECT customer_id, SUM(amount) AS total_spent
    FROM orders
    GROUP BY customer_id
) AS order_summary
WHERE total_spent > 600;

-- =============================================
-- 8. NESTED SUBQUERY
-- Customers who placed orders above average order amount
-- =============================================
SELECT *
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
    WHERE amount > (
        SELECT AVG(amount)
        FROM orders
    )
);
