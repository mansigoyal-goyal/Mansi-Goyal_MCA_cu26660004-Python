import sqlite3

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM students
ORDER BY marks DESC
LIMIT 1
""")

topper = cursor.fetchone()

if topper:
    print("Top student:", topper)
else:
    print("No records found")

conn.close()