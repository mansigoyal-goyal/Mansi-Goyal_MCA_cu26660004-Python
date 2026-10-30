import sqlite3

def insert_student(student_id, name, age, marks):
    conn = sqlite3.connect("student_db.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        marks REAL
    )
    """)

    cursor.execute(
        "INSERT OR IGNORE INTO students VALUES (?, ?, ?, ?)",
        (student_id, name, age, marks)
    )

    conn.commit()
    conn.close()

def fetch_students():
    conn = sqlite3.connect("student_db.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

    conn.close()

insert_student(10, "Rahul", 21, 89)
fetch_students()