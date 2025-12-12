SHOW DATABASES;

CREATE DATABASE IF NOT EXISTS College;
USE College;

CREATE TABLE Teachers(
	id INT PRIMARY KEY,
    name VARCHAR(100),
    subject VARCHAR(100),
    salary INT
);

INSERT INTO Teachers
(id, name, subject, salary)
VALUES
(23, "Ajay", "Math", 50000),
(47, "Bharat", "English", 60000),
(18, "Chetan", "Chemistry", 45000),
(9, "Divya", "Physics", 75000);

SELECT * FROM Teachers;

-- Operatons:
SELECT * FROM Teachers WHERE Salary > 55000;
ALTER TABLE Teachers CHANGE COLUMN Salary CTC INT;
UPDATE Teachers SET CTC = CTC + CTC * 0.25;
SET SQL_SAFE_UPDATES = 0;
ALTER TABLE Teachers ADD COLUMN City VARCHAR(50) DEFAULT "Durgapur";
ALTER TABLE Teachers DROP COLUMN CTC;
