import sqlite3

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS students")

conn.commit()
print("Table deleted")
conn.close()