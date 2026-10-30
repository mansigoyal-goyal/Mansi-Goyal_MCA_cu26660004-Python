with open("sample.txt", "r") as file:
    words = file.read().split()

# Remove duplicate words while preserving order
unique_words = list(dict.fromkeys(words))

with open("unique.txt", "w") as file:
    file.write(" ".join(unique_words))

print("Unique words saved")