import sqlite3

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

cursor.execute("""
SELECT students.name, courses.course_name
FROM students
INNER JOIN courses ON students.id = courses.student_id
""")

for record in cursor.fetchall():
    print(record)

conn.close()