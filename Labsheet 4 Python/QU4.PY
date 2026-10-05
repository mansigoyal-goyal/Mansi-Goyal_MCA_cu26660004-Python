# Find product of all elements in a list

numbers = list(map(int, input("Enter list elements: ").split()))

product = 1

for num in numbers:
    product = product * num

print("Product =", product)