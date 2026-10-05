# Program to sort list in ascending and descending order

numbers = list(map(int, input("Enter numbers: ").split()))

# Bubble sort
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("Ascending order:", numbers)

# Descending order
descending = numbers[::-1]

print("Descending order:", descending)