# Flatten a nested list

nested_list = [[1, 2], [3, 4], [5, 6]]

flat_list = []

for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)

print("Nested List:", nested_list)
print("Flattened List:", flat_list)