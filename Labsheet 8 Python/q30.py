import sqlite3

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
conn.commit()

while True:
    print("\n1. Add student")
    print("2. View students")
    print("3. Update marks")
    print("4. Delete student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = int(input("Enter ID: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))

        cursor.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?)",
            (sid, name, age, marks)
        )
        conn.commit()
        print("Student added")

    elif choice == "2":
        cursor.execute("SELECT * FROM students")
        for row in cursor.fetchall():
            print(row)

    elif choice == "3":
        sid = int(input("Enter ID: "))
        marks = float(input("Enter new marks: "))

        cursor.execute(
            "UPDATE students SET marks = ? WHERE id = ?",
            (marks, sid)
        )
        conn.commit()
        print("Student updated")

    elif choice == "4":
        sid = int(input("Enter ID: "))

        cursor.execute("DELETE FROM students WHERE id = ?", (sid,))
        conn.commit()
        print("Student deleted")

    elif choice == "5":
        break

    else:
        print("Invalid choice")

conn.close()