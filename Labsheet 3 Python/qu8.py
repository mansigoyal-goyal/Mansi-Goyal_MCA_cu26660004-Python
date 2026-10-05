# Program to convert a string into title case

s = input("Enter a string: ")

result = ""
new_word = True

for ch in s:
    if ch == " ":
        result = result + ch
        new_word = True
    else:
        if new_word:
            result = result + ch.upper()
            new_word = False
        else:
            result = result + ch.lower()

print("Title case:", result)