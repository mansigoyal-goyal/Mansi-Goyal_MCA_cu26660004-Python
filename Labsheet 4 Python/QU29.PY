# Find common keys between two dictionaries

dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "b": 40,
    "c": 50,
    "d": 60
}

common_keys = []

for key in dict1:
    if key in dict2:
        common_keys.append(key)

print("Common keys:", common_keys)