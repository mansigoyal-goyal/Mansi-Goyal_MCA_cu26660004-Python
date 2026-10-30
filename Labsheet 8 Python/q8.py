import sqlite3

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    marks REAL
)
""")

cursor.execute(
    "INSERT INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
    (1, "Aman", 20, 85)
)

conn.commit()
print("Record inserted")
conn.close()