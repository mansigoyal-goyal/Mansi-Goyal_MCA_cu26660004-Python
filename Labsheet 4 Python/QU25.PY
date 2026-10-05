# Count frequency of words in a paragraph

paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequency:")

for word in frequency:
    print(word, ":", frequency[word])