# Create nested dictionary for student details

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    roll = input("\nEnter roll number: ")
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))

    students[roll] = {
        "Name": name,
        "Roll": roll,
        "Marks": marks
    }

print("\nStudent Details:")

for roll in students:
    print(students[roll])