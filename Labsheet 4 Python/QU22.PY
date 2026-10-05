# Create dictionary with numbers and their squares

n = int(input("Enter the value of n: "))

squares = {}

for i in range(1, n + 1):
    squares[i] = i * i

print("Dictionary:", squares)