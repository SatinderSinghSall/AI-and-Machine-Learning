USE College;

CREATE TABLE Students(
	roll_no INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(50),
    marks INT
);

INSERT INTO Students
(roll_no, name, city, marks)
VALUES
(100, "Adam", "Delhi", 76),
(108, "Bob", "Mumbai", 65),
(124, "Cascey", "Pune", 94),
(112, "Duke", "Pune", 80);

SELECT * FROM Students;

-- Operations:
SELECT * FROM Students WHERE Marks > 75;
SELECT DISTINCT City FROM students;
SELECT City, MAX(marks) FROM students;
SELECT AVG(marks) FROM Students;

ALTER TABLE students ADD COLUMN Grade VARCHAR(2);

UPDATE Students SET Grade = "o"
WHERE Marks >= 80;

UPDATE Students SET Grade = "o"
WHERE Marks >= 70 AND marks < 80;

UPDATE Students SET Grade = "o"
WHERE Marks >= 80;
