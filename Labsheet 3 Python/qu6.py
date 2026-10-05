# Program to find frequency of each character

s = input("Enter a string: ")

checked = ""

for ch in s:
    if ch not in checked:
        count = 0

        for x in s:
            if x == ch:
                count = count + 1

        print(ch, "=", count)
        checked = checked + ch