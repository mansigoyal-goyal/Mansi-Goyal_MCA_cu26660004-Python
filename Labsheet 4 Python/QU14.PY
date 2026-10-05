# Merge two dictionaries

dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}

merged = {}

for key in dict1:
    merged[key] = dict1[key]

for key in dict2:
    merged[key] = dict2[key]

print("Merged Dictionary:", merged)