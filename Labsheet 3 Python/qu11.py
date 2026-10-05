# Program to check whether two strings are anagrams

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

s1 = s1.lower()
s2 = s2.lower()

if len(s1) != len(s2):
    print("The strings are not anagrams.")
else:
    count1 = {}
    count2 = {}

    for ch in s1:
        if ch in count1:
            count1[ch] = count1[ch] + 1
        else:
            count1[ch] = 1

    for ch in s2:
        if ch in count2:
            count2[ch] = count2[ch] + 1
        else:
            count2[ch] = 1

    if count1 == count2:
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")