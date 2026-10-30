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

conn.commit()
print("Students table created")
conn.close()