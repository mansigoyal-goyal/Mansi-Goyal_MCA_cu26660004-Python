# Create a list of squares from 1 to n

n = int(input("Enter the value of n: "))

squares = []

for i in range(1, n + 1):
    squares.append(i * i)

print("List of squares:", squares)