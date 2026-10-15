
# Flatten a nested tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))

result = tuple(item for subtuple in nested_tuple
               for item in subtuple)

print("Flattened tuple:", result)
