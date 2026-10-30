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

records = [
    (1, "Aman", 20, 85),
    (2, "Riya", 21, 92),
    (3, "Neha", 20, 78)
]

cursor.executemany("""
INSERT OR IGNORE INTO students VALUES (?, ?, ?, ?)
""", records)

conn.commit()
print("Records inserted")
conn.close()