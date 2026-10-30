import sqlite3

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

roll = int(input("Enter student ID: "))

cursor.execute("DELETE FROM students WHERE id = ?", (roll,))

conn.commit()
print("Rows deleted:", cursor.rowcount)
conn.close()