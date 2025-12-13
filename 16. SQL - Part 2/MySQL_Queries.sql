SHOW DATABASES;

SELECT @@AUTOCOMMIT;
SET AUTOCOMMIT = 0;
SET AUTOCOMMIT = 1;

USE College;
SHOW Tables;

CREATE TABLE Accounts(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    balance INT(2)
);

INSERT IN TO Accounts
(name, balance)
VALUES
("Adam", 500.00),
("Bob", 300.00),
("Charlie", 1000.00);

SELECT * FROM Accounts;

-- Transcation Commands: COMMIT
START TRANSACTION;
UPDATE Accounts SET balance = balance - 50 WHERE id = 1;
UPDATE Accounts SET balance = balance + 50 WHERE id = 2;
COMMIT;

SELECT * FROM Accounts;

-- Transcation Commands: ROLLBACK
START TRANSACTION;
UPDATE Accounts SET balance = balance - 50 WHERE id = 1;
UPDATE Accounts SET balance = balance + 50 WHERE id = 2;
ROLLBACK;

START TRANSACTION;
UPDATE Accounts SET balance = balance - 50 WHERE id = 1;
COMMIT;
UPDATE Accounts SET balance = balance + 50 WHERE id = 2;
ROLLBACK;

SELECT * FROM Accounts;

-- Savepoint:
START TRANSACTION;
UPDATE Accounts SET balance = balance + 1000 WHERE id = 1;
SAVEPOINT after_wallet_topup;
UPDATE Accounts SET balance = balance + 10 WHERE id = 1;
ROLLBACK TO after_wallet_topup;
COMMIT;

SELECT * FROM Accounts;

-- JOINTS in SQL:
