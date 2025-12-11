SHOW DATABASES;
CREATE DATABASE Instagram;
USE Instagram;

CREATE TABLE Users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    age INT CHECK (age >= 0),
    email VARCHAR(50) UNIQUE,
    followers INT DEFAULT 0,
    following INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Posts(
    id INT PRIMARY KEY AUTO_INCREMENT,
    content VARCHAR(900) NOT NULL,
    user_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id)
        ON DELETE CASCADE
);

-- Index for faster user → posts lookup
CREATE INDEX idx_posts_user ON Posts(user_id);

CREATE TABLE Likes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    post_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id)
        ON DELETE CASCADE,
    FOREIGN KEY (post_id) REFERENCES Posts(id)
        ON DELETE CASCADE,
    UNIQUE(user_id, post_id) -- prevents liking the same post twice
);

CREATE INDEX idx_likes_user ON Likes(user_id);
CREATE INDEX idx_likes_post ON Likes(post_id);

CREATE TABLE Comments(
    id INT PRIMARY KEY AUTO_INCREMENT,
    comment_text VARCHAR(300) NOT NULL,
    user_id INT,
    post_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id)
        ON DELETE CASCADE,
    FOREIGN KEY (post_id) REFERENCES Posts(id)
        ON DELETE CASCADE
);

CREATE INDEX idx_comments_user ON Comments(user_id);
CREATE INDEX idx_comments_post ON Comments(post_id);

INSERT INTO Users (name, age, email, followers, following)
VALUES
('Alice Johnson', 22, 'alice@example.com', 120, 150),
('Bob Smith', 27, 'bob@example.com', 300, 280),
('Charlie Brown', 19, 'charlie@example.com', 90, 100),
('Diana Parker', 30, 'diana@example.com', 500, 450);

INSERT INTO Posts (content, user_id)
VALUES
('Enjoying a sunny day at the beach! ☀️', 1),
('Just finished a 10k run 🏃‍♂️💨', 2),
('Learning SQL is fun! 😄', 3),
('New coffee recipe experiment ☕🔥', 4),
('Reading a great book today 📚', 1);

INSERT INTO Likes (user_id, post_id)
VALUES
(1, 2),
(2, 1),
(3, 1),
(4, 1),
(2, 3),
(1, 4);

INSERT INTO Comments (comment_text, user_id, post_id)
VALUES
('Looks amazing! 😍', 2, 1),
('Great job!', 1, 2),
('Totally agree!', 4, 3),
('What book are you reading?', 3, 5),
('Nice coffee shot! ☕', 2, 4);

SELECT * FROM Users;
SELECT * FROM Posts;
SELECT * FROM Likes;
SELECT * FROM Comments;
