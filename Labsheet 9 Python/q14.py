import sqlite3

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

roll = int(input("Enter student ID: "))

cursor.execute("SELECT * FROM students WHERE id = ?", (roll,))
record = cursor.fetchone()

if record:
    print(record)
else:
    print("Student not found")

conn.close()