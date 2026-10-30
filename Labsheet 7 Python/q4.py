with open("sample.txt", "r") as file:
    content = file.read()

# Split text into words
words = content.split()

print("Number of words:", len(words))