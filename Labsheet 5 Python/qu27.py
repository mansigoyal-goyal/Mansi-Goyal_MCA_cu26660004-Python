
# Unzip a list of tuples
my_list = [(1, 'A'), (2, 'B'), (3, 'C')]

numbers, letters = zip(*my_list)

print("Numbers:", list(numbers))
print("Letters:", list(letters))
