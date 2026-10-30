import sqlite3

try:
    conn = sqlite3.connect("student_db.db")
    print("Database connected successfully")
    conn.close()
except sqlite3.Error as e:
    print("Database error:", e)