# Create a dictionary of student names and marks

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

print("\nStudent Dictionary:")

for name in students:
    print(name, ":", students[name])