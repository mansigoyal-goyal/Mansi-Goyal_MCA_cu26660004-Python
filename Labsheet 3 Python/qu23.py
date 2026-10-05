# Program to remove duplicate elements

numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("List after removing duplicates:", result)