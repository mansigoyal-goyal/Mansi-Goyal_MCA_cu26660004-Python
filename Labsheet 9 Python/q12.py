import sqlite3

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO students VALUES (?, ?, ?, ?)",
    (20, "Karan", 21, 88)
)

conn.commit()
print("Record inserted")
conn.close()