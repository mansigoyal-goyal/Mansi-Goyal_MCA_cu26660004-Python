# Split a list into two halves

numbers = list(map(int, input("Enter list elements: ").split()))

middle = len(numbers) // 2

first_half = numbers[:middle]
second_half = numbers[middle:]

print("First Half:", first_half)
print("Second Half:", second_half)