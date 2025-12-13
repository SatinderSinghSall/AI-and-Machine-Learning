SHOW DATABASES;

CREATE DATABASE ECommerce;
USE ECommerce;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);

INSERT INTO customers VALUES
(1, 'Alice', 'Mumbai'),
(2, 'Bob', 'Delhi'),
(3, 'Charlie', 'Bangalore'),
(4, 'David', 'Mumbai');

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    amount INT
);

INSERT INTO orders VALUES
(101, 1, 500),
(102, 1, 900),
(103, 2, 300),
(104, 5, 700);

SELECT * FROM Customers;
SELECT * FROM Orders;

-- JOINTS in SQL:

-- INNER JOIN
SELECT * FROM Customers C INNER JOIN Orders O ON C.customer_id = O.customer_id;

-- LEFT & RIGHT JOIN
SELECT * FROM Customers C LEFT JOIN Orders O ON C.customer_id = O.customer_id;
SELECT * FROM Customers C RIGHT JOIN Orders O ON C.customer_id = O.customer_id;

-- OUTER JOIN & CROSS JOIN
SELECT *
FROM Customers C
LEFT JOIN Orders O
ON C.customer_id = O.customer_id

UNION

SELECT *
FROM Customers C
RIGHT JOIN Orders O
ON C.customer_id = O.customer_id;


SELECT *
FROM Customers
CROSS JOIN Orders;

-- SELF JOIN
SELECT 
    C1.name AS Customer1,
    C2.name AS Customer2,
    C1.city
FROM Customers C1
INNER JOIN Customers C2
ON C1.city = C2.city
AND C1.customer_id < C2.customer_id;

SELECT 
    C1.name,
    C2.name,
    C1.city,
    C2.city
FROM Customers C1
JOIN Customers C2
ON C1.city <> C2.city;

-- Practice Problem:
SELECT C.customer_id, C.name, C.city, NULL AS order_id, NULL AS amount
FROM Customers C
LEFT JOIN Orders O
ON C.customer_id = O.customer_id
WHERE O.customer_id IS NULL

UNION

SELECT NULL, NULL, NULL, O.order_id, O.amount
FROM Customers C
RIGHT JOIN Orders O
ON C.customer_id = O.customer_id
WHERE C.customer_id IS NULL;
