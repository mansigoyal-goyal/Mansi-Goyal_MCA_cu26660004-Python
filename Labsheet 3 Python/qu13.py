# Program to convert vowels to uppercase and consonants to lowercase

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            result = result + ch.upper()
        else:
            result = result + ch.lower()
    else:
        result = result + ch

print("Result:", result)