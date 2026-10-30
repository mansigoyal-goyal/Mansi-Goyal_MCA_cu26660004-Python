import csv

with open("students.csv", "r", newline="") as file:
    rows = list(csv.reader(file))

if rows:
    print("Number of data rows:", len(rows) - 1)
    print("Number of columns:", len(rows[0]))
else:
    print("CSV file is empty")