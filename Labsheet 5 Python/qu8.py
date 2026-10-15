
# Find the index of an element
my_tuple = (10, 20, 30, 40, 50)

element = int(input("Enter an element: "))

if element in my_tuple:
    print("Index:", my_tuple.index(element))
else:
    print("Element not found")
