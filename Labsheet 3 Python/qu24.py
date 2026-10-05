# Program to reverse a list

numbers = list(map(int, input("Enter numbers: ").split()))

left = 0
right = len(numbers) - 1

while left < right:
    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp

    left = left + 1
    right = right - 1

print("Reversed list:", numbers)