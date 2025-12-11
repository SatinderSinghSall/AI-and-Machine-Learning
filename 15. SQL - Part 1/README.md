# 📚 **Instagram MySQL Database — Full Documentation (Basic → Advanced)**

A fully relational MySQL database designed to simulate a simplified **Instagram-like social media platform**.
This README explains the schema, relationships, SQL concepts used, and advanced extensions.

---

# 📌 **Table of Contents**

1. [Overview](#overview)
2. [Database Features](#database-features)
3. [Schema Structure](#schema-structure)
4. [Entity-Relationship Diagram (ERD)](#entity-relationship-diagram-erd)
5. [SQL Concepts Covered](#sql-concepts-covered)
6. [Installation & Setup](#installation--setup)
7. [Tables Breakdown](#tables-breakdown)
8. [Sample Queries (Basic → Advanced)](#sample-queries-basic--advanced)
9. [Indexes & Performance](#indexes--performance)
10. [Data Integrity & Constraints](#data-integrity--constraints)
11. [Future Enhancements](#future-enhancements)
12. [License](#license)

---

# 🚀 **Overview**

This project demonstrates how to design and implement a complete **relational MySQL database** for a social media platform.
It includes:

- Users
- Posts
- Likes
- Comments

The schema is optimized with **indexes**, **foreign keys**, and **constraints** to model real-world relationships.

---

# ⭐ **Database Features**

- Fully relational structure
- Cascading relationships
- Unique + check constraints
- Indexed foreign keys for performance
- Many-to-many mapping using a junction table (`Likes`)
- Auto-maintained timestamps
- Example data (Users, Posts, Likes, Comments)

---

# 🧱 **Schema Structure**

### **Database Name**

```
Instagram
```

### **Tables**

| Table Name   | Purpose                     |
| ------------ | --------------------------- |
| **Users**    | Stores user profiles        |
| **Posts**    | Stores user-generated posts |
| **Likes**    | Maps users liking posts     |
| **Comments** | Stores comments on posts    |

---

# 🔗 **Entity-Relationship Diagram (ERD)**

```
 Users (1) ───< Posts (∞)
    │              │
    │              └────< Comments (∞)
    │
    └────< Likes (∞) >──── Posts
```

Relationship summary:

- **1 User → Many Posts**
- **1 User → Many Comments**
- **1 User → Many Likes**
- **1 Post → Many Likes**
- **1 Post → Many Comments**
- Likes = Many-to-Many between Users & Posts

---

# 🧠 **SQL Concepts Covered**

### **Basic SQL**

- CREATE DATABASE
- CREATE TABLE
- INSERT, SELECT
- Data types (`INT`, `VARCHAR`, `TIMESTAMP`, etc.)

### **Intermediate SQL**

- Primary keys
- Foreign keys
- `AUTO_INCREMENT`
- Unique constraints
- Check constraints
- Default values
- Index creation
- Cascade deletion

### **Advanced SQL**

- Many-to-many relationships
- Query optimization with indexes
- JOIN queries across multiple tables
- Aggregation & analytics
- Query design patterns for social apps
- Normalized relational schema

---

# 🛠 **Installation & Setup**

### **1. Create the database**

```sql
CREATE DATABASE Instagram;
USE Instagram;
```

### **2. Create tables**

(Use your full schema script — included here)

```sql
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
    UNIQUE(user_id, post_id)
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
```

### **3. Insert sample data**

```sql
INSERT INTO Users (name, age, email, followers, following)
VALUES
('Alice Johnson', 22, 'alice@example.com', 120, 150),
('Bob Smith', 27, 'bob@example.com', 300, 280),
('Charlie Brown', 19, 'charlie@example.com', 90, 100),
('Diana Parker', 30, 'diana@example.com', 500, 450);
```

(Posts, Likes, and Comments inserts remain the same.)

---

# 📄 **Tables Breakdown**

## **1. Users Table**

Fields include:

- User identity
- Age validation (`CHECK`)
- Unique email
- Follower/following counters
- Creation timestamp

## **2. Posts Table**

- Each post belongs to a user
- Cascade delete removes posts when a user is removed

## **3. Likes Table**

- Many-to-many mapping
- `UNIQUE(user_id, post_id)` prevents duplicate likes

## **4. Comments Table**

- Stores all post comments
- Cascade delete removes comments when post/user is deleted

---

# 🔍 **Sample Queries (Basic → Advanced)**

## **Basic**

### Get all users

```sql
SELECT * FROM Users;
```

### Get posts by a specific user

```sql
SELECT * FROM Posts WHERE user_id = 1;
```

---

## **Intermediate**

### Find all likes on a post

```sql
SELECT u.name
FROM Likes l
JOIN Users u ON l.user_id = u.id
WHERE l.post_id = 1;
```

### Count comments on each post

```sql
SELECT post_id, COUNT(*) AS comment_count
FROM Comments
GROUP BY post_id;
```

---

## **Advanced**

### Get the most popular post (by likes)

```sql
SELECT p.id, p.content, COUNT(l.id) AS total_likes
FROM Posts p
LEFT JOIN Likes l ON p.id = l.post_id
GROUP BY p.id
ORDER BY total_likes DESC
LIMIT 1;
```

### Get full post feed including author, likes, comments

```sql
SELECT
    p.id AS post_id,
    u.name AS author,
    p.content,
    (SELECT COUNT(*) FROM Likes WHERE post_id = p.id) AS likes,
    (SELECT COUNT(*) FROM Comments WHERE post_id = p.id) AS comments
FROM Posts p
JOIN Users u ON p.user_id = u.id
ORDER BY p.created_at DESC;
```

---

# ⚡ **Indexes & Performance**

Indexes created:

- `Posts(user_id)`
- `Likes(user_id)`, `Likes(post_id)`
- `Comments(user_id)`, `Comments(post_id)`

**Why?**

- Faster joins on foreign keys
- Faster analytics queries
- Better feed performance

---

# 🛡 **Data Integrity & Constraints**

| Type                | Purpose                              |
| ------------------- | ------------------------------------ |
| `PRIMARY KEY`       | Uniquely identifies a row            |
| `FOREIGN KEY`       | Ensures valid relationships          |
| `ON DELETE CASCADE` | Automatically removes dependent rows |
| `UNIQUE`            | Prevent duplicate emails/likes       |
| `CHECK`             | Validates age                        |
| `DEFAULT`           | Auto-generates values                |

---

# 🚧 **Future Enhancements**

Potential upgrades:

### 🔹 Advanced Social Features

- Followers table
- Saved posts
- Direct messages

### 🔹 Analytics

- Trend detection
- User engagement scoring

### 🔹 Security

- Password hashing
- Role-based access

### 🔹 Performance

- Composite indexes
- Partitioning for large datasets

---

# 📜 **License**

This project is open-source and free to use for learning and development.

---
