# Program to replace spaces with underscores

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch == " ":
        result = result + "_"
    else:
        result = result + ch

print("String after replacement:", result)