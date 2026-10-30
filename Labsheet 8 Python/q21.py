import sqlite3

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT,
    student_id INTEGER
)
""")

cursor.execute("""
INSERT OR IGNORE INTO courses
VALUES (?, ?, ?)
""", (101, "Python", 1))

conn.commit()
print("Course created and data inserted")
conn.close()