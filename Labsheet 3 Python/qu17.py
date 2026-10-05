# Program to print all substrings

s = input("Enter a string: ")

print("All substrings:")

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        print(s[i:j])