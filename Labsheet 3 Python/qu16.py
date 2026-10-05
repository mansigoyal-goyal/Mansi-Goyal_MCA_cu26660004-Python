# Program to count digits, alphabets and special characters

s = input("Enter a string: ")

alphabets = 0
digits = 0
special = 0

for ch in s:
    if ch.isalpha():
        alphabets = alphabets + 1
    elif ch.isdigit():
        digits = digits + 1
    else:
        special = special + 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Special characters:", special)