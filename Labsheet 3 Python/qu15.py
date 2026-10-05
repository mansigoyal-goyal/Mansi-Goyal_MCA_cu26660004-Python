# Program to find first non-repeated character

s = input("Enter a string: ")

found = False

for ch in s:
    count = 0

    for x in s:
        if x == ch:
            count = count + 1

    if count == 1:
        print("First non-repeated character:", ch)
        found = True
        break

if found == False:
    print("No non-repeated character found.")