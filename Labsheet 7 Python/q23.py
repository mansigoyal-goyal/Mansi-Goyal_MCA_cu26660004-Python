import csv

marks = []

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        marks.append(float(row["Marks"]))

if marks:
    print("Average marks:", sum(marks) / len(marks))
else:
    print("No records found")