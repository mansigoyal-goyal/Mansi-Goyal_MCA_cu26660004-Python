with open("numbers.txt", "r") as file:
    numbers = [float(x) for x in file.read().split()]

if numbers:
    print("Sum:", sum(numbers))
    print("Average:", sum(numbers) / len(numbers))
else:
    print("No numbers found")