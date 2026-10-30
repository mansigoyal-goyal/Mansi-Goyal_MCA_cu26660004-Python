word = input("Enter word: ")

with open("sample.txt", "r") as file:
    words = file.read().lower().split()

count = words.count(word.lower())

print("Occurrences:", count)