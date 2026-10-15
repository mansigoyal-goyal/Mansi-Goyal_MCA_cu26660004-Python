
s1 = input("Enter first string: ").lower().replace(" ", "")
s2 = input("Enter second string: ").lower().replace(" ", "")

if len(s1) == len(s2) and sorted(s1) == sorted(s2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")
