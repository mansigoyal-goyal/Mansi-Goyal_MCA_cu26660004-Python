
# Check whether all elements are the same
my_tuple = (5, 5, 5, 5, 5)

if all(x == my_tuple[0] for x in my_tuple):
    print("All elements are the same")
else:
    print("Elements are different")
