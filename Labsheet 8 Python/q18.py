import sqlite3

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

student_id = int(input("Enter student ID: "))

cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))

conn.commit()
print("Rows deleted:", cursor.rowcount)
conn.close()