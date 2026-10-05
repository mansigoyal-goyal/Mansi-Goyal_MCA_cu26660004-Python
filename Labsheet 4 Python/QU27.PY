# Remove duplicate values from dictionary

data = {
    "A": 10,
    "B": 20,
    "C": 10,
    "D": 30,
    "E": 20
}

result = {}

for key in data:
    value = data[key]

    if value not in result.values():
        result[key] = value

print("Original Dictionary:", data)
print("After removing duplicate values:", result)