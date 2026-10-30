import sqlite3

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

cursor.execute("""
SELECT name FROM sqlite_master
WHERE type = 'table' AND name = ?
""", ("students",))

if cursor.fetchone():
    print("Table exists")
else:
    print("Table does not exist")

conn.close()