students = [
    "1,Aman,85",
    "2,Riya,92"
]

with open("student_data.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

with open("student_data.txt", "r") as file:
    print(file.read())