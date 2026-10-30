import sqlite3

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM students WHERE marks < ?", (40,))

conn.commit()
print("Rows deleted:", cursor.rowcount)
conn.close()