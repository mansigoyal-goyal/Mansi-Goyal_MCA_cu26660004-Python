import sqlite3
import csv

conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

with open("students_export.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Age", "Marks"])
    writer.writerows(rows)

conn.close()
print("Data exported to CSV")