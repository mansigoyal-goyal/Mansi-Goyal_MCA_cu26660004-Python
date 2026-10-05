# Sort dictionary by keys

data = {"banana": 20, "apple": 10, "mango": 30}

sorted_data = dict(sorted(data.items()))

print("Dictionary sorted by keys:")

for key in sorted_data:
    print(key, ":", sorted_data[key])