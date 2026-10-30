students = [
    {"roll": 1, "name": "Aman", "marks": 85},
    {"roll": 2, "name": "Riya", "marks": 92}
]

roll = int(input("Enter roll number: "))
new_marks = float(input("Enter new marks: "))

for student in students:
    if student["roll"] == roll:
        student["marks"] = new_marks
        print("Marks updated")
        break
else:
    print("Student not found")

print(students)