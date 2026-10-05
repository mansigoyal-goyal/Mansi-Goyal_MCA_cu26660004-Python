# Program to check whether two strings are rotations

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("The strings are rotations of each other.")
else:
    print("The strings are not rotations of each other.")