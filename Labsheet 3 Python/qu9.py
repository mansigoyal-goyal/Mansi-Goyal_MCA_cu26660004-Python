# Program to count words in a string

s = input("Enter a string: ")

count = 0
inside_word = False

for ch in s:
    if ch != " " and inside_word == False:
        count = count + 1
        inside_word = True
    elif ch == " ":
        inside_word = False

print("Number of words:", count)