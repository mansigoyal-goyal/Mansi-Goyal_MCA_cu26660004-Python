# Find sum of all dictionary values

marks = {
    "Mansi": 85,
    "Rahul": 78,
    "Priya": 92
}

total = 0

for value in marks.values():
    total += value

print("Sum of all values:", total)