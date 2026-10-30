import csv

with open("students.csv", "r", newline="") as source:
    rows = list(csv.reader(source))

with open("students_copy.csv", "w", newline="") as destination:
    writer = csv.writer(destination)
    writer.writerows(rows)

print("CSV data copied successfully")