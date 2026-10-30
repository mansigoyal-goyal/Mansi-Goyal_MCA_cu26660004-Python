word = input("Enter word to search: ")

with open("sample.txt", "r") as file:
    content = file.read().split()

if word in content:
    print("Word found")
else:
    print("Word not found")