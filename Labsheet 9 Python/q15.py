import sqlite3

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

roll = int(input("Enter student ID: "))
marks = float(input("Enter new marks: "))

cursor.execute(
    "UPDATE students SET marks = ? WHERE id = ?",
    (marks, roll)
)

conn.commit()
print("Rows updated:", cursor.rowcount)
conn.close()