# Program to sort characters alphabetically

s = input("Enter a string: ")

characters = list(s)

# Bubble sort
for i in range(len(characters)):
    for j in range(0, len(characters) - i - 1):
        if characters[j] > characters[j + 1]:
            temp = characters[j]
            characters[j] = characters[j + 1]
            characters[j + 1] = temp

result = ""

for ch in characters:
    result = result + ch

print("Sorted string:", result)