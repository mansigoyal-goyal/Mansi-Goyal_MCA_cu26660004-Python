import sqlite3

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

cursor.execute("SELECT AVG(marks) FROM students")
print("Average marks:", cursor.fetchone()[0])

conn.close()