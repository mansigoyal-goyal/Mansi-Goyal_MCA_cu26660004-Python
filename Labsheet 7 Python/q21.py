import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Marks"])
    writer.writerow([1, "Aman", 85])
    writer.writerow([2, "Riya", 92])

print("CSV file created")