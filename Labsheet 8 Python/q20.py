import sqlite3

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM students")

conn.commit()
print("Table emptied")
conn.close()