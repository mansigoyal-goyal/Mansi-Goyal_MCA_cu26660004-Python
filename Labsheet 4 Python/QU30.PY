# Create dictionary with characters as keys
# and their frequency as values

text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character Frequency Dictionary:")

for char in frequency:
    print(char, ":", frequency[char])