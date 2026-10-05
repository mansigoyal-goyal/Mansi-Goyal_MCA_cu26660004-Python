# Program to reverse a string without using slicing

s = input("Enter a string: ")

reverse = ""

for i in range(len(s) - 1, -1, -1):
    reverse = reverse + s[i]

print("Reversed string:", reverse)