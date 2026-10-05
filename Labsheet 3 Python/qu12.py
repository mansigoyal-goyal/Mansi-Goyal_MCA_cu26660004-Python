# Program to check whether substring exists

s = input("Enter main string: ")
sub = input("Enter substring: ")

if sub in s:
    print("Substring exists in the string.")
else:
    print("Substring does not exist.")