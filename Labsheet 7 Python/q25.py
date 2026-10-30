import csv

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([3, "Neha", 88])

print("Record added successfully")