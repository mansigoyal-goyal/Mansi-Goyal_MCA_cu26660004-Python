import sqlite3
import csv

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

with open("students_import.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute("""
        INSERT OR IGNORE INTO students
        VALUES (?, ?, ?, ?)
        """, (
            int(row["ID"]),
            row["Name"],
            int(row["Age"]),
            float(row["Marks"])
        ))

conn.commit()
conn.close()
print("CSV data imported")