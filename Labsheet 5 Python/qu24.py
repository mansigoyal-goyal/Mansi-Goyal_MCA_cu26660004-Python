
# Find common elements
tuple1 = (10, 20, 30, 40)
tuple2 = (30, 40, 50, 60)

common = tuple(x for x in tuple1 if x in tuple2)

print("Common elements:", common)
