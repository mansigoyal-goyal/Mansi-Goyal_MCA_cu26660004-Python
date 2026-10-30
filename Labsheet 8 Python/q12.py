import sqlite3

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students WHERE marks > ?", (80,))

for record in cursor.fetchall():
    print(record)

conn.close()