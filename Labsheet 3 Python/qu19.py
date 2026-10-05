# Program to find the most repeated word

s = input("Enter a sentence: ")

words = s.lower().split()

most_word = ""
max_count = 0

for word in words:
    count = 0

    for x in words:
        if word == x:
            count = count + 1

    if count > max_count:
        max_count = count
        most_word = word

print("Most repeated word:", most_word)
print("Frequency:", max_count)