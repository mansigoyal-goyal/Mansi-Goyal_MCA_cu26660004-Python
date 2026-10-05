# Convert a list into a string without using join()

items = input("Enter list elements separated by spaces: ").split()

result = ""

for item in items:
    result = result + item

print("String:", result)