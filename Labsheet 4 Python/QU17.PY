# Update the value of a key

students = {
    "Mansi": 85,
    "Rahul": 78,
    "Priya": 92
}

key = input("Enter student name to update: ")

if key in students:
    new_marks = float(input("Enter new marks: "))
    students[key] = new_marks
    print("Value updated successfully.")
else:
    print("Key not found.")

print("Dictionary:", students)