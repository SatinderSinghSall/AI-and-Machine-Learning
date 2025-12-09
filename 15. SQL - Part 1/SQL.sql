SHOW DATABASES;
CREATE DATABASE satinder_database_2;
USE satinder_database_2;
DROP DATABASE satinder_database_2;

CREATE DATABASE satinder_college;
USE satinder_college;

CREATE TABLE Students(
	stuRoll_no INT,
    stuName VARCHAR(50),
    stuAge INT
);

INSERT INTO Students
VALUES
(001, "Satinder Singh Sall", 22);

INSERT INTO Students
VALUES
(002, "Soni Vaibhav Kumar", 19),
(003, "Swayam Kehsarwani", 22),
(004, "Harsha HM", 22),
(005, "K Santosh Reddy", 22);

SELECT * FROM Students;

DROP TABLE Students;
