students = [
    {"roll": 1, "name": "Aman", "marks": 85},
    {"roll": 2, "name": "Riya", "marks": 92}
]

name = input("Enter student name: ").strip().lower()

for student in students:
    if student["name"].lower() == name:
        print(student)
        break
else:
    print("Student not found")