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

CREATE TABLE Users(
	id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    email VARCHAR(50) UNIQUE,
    followers INT DEFAULT 0,
    following INT DEFAULT 0,

    CONSTRAINT age_check CHECK (age >= 0)
);

CREATE TABLE Post(
	id INT PRIMARY KEY,
    Content VARCHAR(900) NOT NULL,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

INSERT INTO Users VALUES
(1, "Satinder Singh Sall", "satindersinghsall111@gmail.com", 500, 50),
(2, "Soni Vaibhav Kumar", "sonivaibhavkumargmail.com", 200, 30),
(3, "K Santosh Reddy", "ksantoshreddy@gmail.com", 500, 50);

SELECT * FROM Users;
