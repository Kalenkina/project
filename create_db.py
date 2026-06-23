import psycopg2

conn = psycopg2.connect(
    database="user",
    user="postgres",
    password="***",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    username VARCHAR(100),
    created_at DATE
);
""")

cur.execute("""
CREATE TABLE Posts (
    post_id INT PRIMARY KEY,
    author_id INT,
    post_text TEXT,
    published_at TIMESTAMP
);
""")

cur.execute("""
CREATE TABLE Activities (
    event_id INT PRIMARY KEY,
    user_id INT,
    action_type VARCHAR(20),
    post_id INT,
    comment_text TEXT,
    activity_time TIMESTAMP
);
""")

cur.execute("""
CREATE INDEX idx_user_action
ON Activities(user_id, action_type);
""")

# cur.execute("""
# DROP TABLE IF EXISTS Activities;
# DROP TABLE IF EXISTS Posts;
# DROP TABLE IF EXISTS Users;
# """)

conn.commit()
conn.close()