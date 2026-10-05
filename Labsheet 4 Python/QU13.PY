# Count frequency of characters

text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character Frequency:")

for char in frequency:
    print(char, ":", frequency[char])