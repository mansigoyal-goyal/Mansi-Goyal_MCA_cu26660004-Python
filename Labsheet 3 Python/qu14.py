# Program to remove punctuation

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch.isalnum() or ch == " ":
        result = result + ch

print("String without punctuation:", result)