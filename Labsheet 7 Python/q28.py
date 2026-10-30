import csv

with open("students.csv", "r", newline="") as file:
    students = list(csv.DictReader(file))

if students:
    topper = max(students, key=lambda s: float(s["Marks"]))
    print("Topper:", topper["Name"])
    print("Highest marks:", topper["Marks"])
else:
    print("No student records found")