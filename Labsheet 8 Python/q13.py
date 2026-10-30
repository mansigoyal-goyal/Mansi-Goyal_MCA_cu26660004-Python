import sqlite3

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students ORDER BY marks DESC")

for record in cursor.fetchall():
    print(record)

conn.close()