students = [
    {"roll": 1, "name": "Aman", "marks": 85},
    {"roll": 2, "name": "Riya", "marks": 92}
]

roll = int(input("Enter roll number to delete: "))

for student in students:
    if student["roll"] == roll:
        students.remove(student)
        print("Student deleted")
        break
else:
    print("Student not found")

print(students)