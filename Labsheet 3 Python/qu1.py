# Program to check whether a string is palindrome

s = input("Enter a string: ")

reverse = ""

# Reverse the string using a loop
for i in range(len(s) - 1, -1, -1):
    reverse = reverse + s[i]

if s == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")