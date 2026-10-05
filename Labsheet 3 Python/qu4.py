# Program to extract uppercase characters

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch.isupper():
        result = result + ch

print("Uppercase characters:", result)