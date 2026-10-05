# Sort dictionary by values

data = {"A": 50, "B": 20, "C": 40, "D": 10}

sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))

print("Dictionary sorted by values:")

for key in sorted_data:
    print(key, ":", sorted_data[key])