# Find key having maximum value

marks = {
    "Mansi": 85,
    "Rahul": 78,
    "Priya": 92
}

maximum = None
max_key = None

for key in marks:
    if maximum is None or marks[key] > maximum:
        maximum = marks[key]
        max_key = key

print("Key with maximum value:", max_key)
print("Maximum value:", maximum)