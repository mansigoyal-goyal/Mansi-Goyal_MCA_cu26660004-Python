# Remove all negative numbers from a list

numbers = list(map(int, input("Enter list elements: ").split()))

positive_list = []

for num in numbers:
    if num >= 0:
        positive_list.append(num)

print("List after removing negative numbers:", positive_list)