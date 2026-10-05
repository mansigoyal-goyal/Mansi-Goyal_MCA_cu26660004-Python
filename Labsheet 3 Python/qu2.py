# Program to count vowels and consonants

s = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in s:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            vowels = vowels + 1
        else:
            consonants = consonants + 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)