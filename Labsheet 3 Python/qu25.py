# Program to count frequency of each element

numbers = list(map(int, input("Enter numbers: ").split()))

checked = []

for num in numbers:
    if num not in checked:
        count = 0

        for x in numbers:
            if x == num:
                count = count + 1

        print(num, "=", count)
        checked.append(num)