import sqlite3

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM students")
print("Total students:", cursor.fetchone()[0])

conn.close()