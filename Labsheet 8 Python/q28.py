import sqlite3

try:
    conn = sqlite3.connect("student_db.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM unknown_table")

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if "conn" in locals():
        conn.close()