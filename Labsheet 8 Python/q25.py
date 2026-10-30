import sqlite3

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

cursor.execute("""
SELECT age, COUNT(*)
FROM students
GROUP BY age
""")

for record in cursor.fetchall():
    print("Age:", record[0], "Students:", record[1])

conn.close()