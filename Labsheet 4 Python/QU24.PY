# Invert a dictionary

data = {
    "a": 1,
    "b": 2,
    "c": 3
}

inverted = {}

for key in data:
    inverted[data[key]] = key

print("Original Dictionary:", data)
print("Inverted Dictionary:", inverted)