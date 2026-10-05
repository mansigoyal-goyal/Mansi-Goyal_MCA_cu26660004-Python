# Rotate a list by n positions

numbers = list(map(int, input("Enter list elements: ").split()))
n = int(input("Enter number of positions: "))

n = n % len(numbers)

rotated_list = numbers[-n:] + numbers[:-n]

print("Original List:", numbers)
print("Rotated List:", rotated_list)