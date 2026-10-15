
# Find repeated items
my_tuple = (10, 20, 10, 30, 20, 40, 10)

repeated = tuple(
    x for i, x in enumerate(my_tuple)
    if x in my_tuple[:i] and x not in my_tuple[:i-1]
)

# Display repeated items only once
result = tuple(dict.fromkeys(
    x for x in my_tuple if my_tuple.count(x) > 1
))

print("Repeated items:", result)
