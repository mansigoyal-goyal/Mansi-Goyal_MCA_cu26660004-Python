import sqlite3

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

student_id = int(input("Enter student ID: "))
new_name = input("Enter new name: ")

cursor.execute(
    "UPDATE students SET name = ? WHERE id = ?",
    (new_name, student_id)
)

conn.commit()
print("Rows updated:", cursor.rowcount)
conn.close()