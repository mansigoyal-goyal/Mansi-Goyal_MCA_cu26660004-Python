# Program to find second largest number

numbers = list(map(int, input("Enter numbers: ").split()))

largest = numbers[0]
second_largest = None

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num != largest:
        if second_largest is None or num > second_largest:
            second_largest = num

if second_largest is None:
    print("Second largest number does not exist.")
else:
    print("Second largest number:", second_largest)