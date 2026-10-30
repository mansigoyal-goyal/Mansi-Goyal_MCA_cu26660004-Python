import csv

name = input("Enter student name: ").strip().lower()
found = False

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Name"].strip().lower() == name:
            print(row)
            found = True

if not found:
    print("Student not found")