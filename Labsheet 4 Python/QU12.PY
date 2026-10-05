# Find maximum and minimum marks without using max() or min()

students = {
    "Mansi": 85,
    "Rahul": 78,
    "Priya": 92,
    "Aman": 88
}

maximum = None
minimum = None

for marks in students.values():

    if maximum is None or marks > maximum:
        maximum = marks

    if minimum is None or marks < minimum:
        minimum = marks

print("Maximum Marks:", maximum)
print("Minimum Marks:", minimum)