import sqlite3

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(students)")

for column in cursor.fetchall():
    print(column)

conn.close()