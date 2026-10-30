with open("sample.txt", "r") as file:
    words = file.read().split()

words.sort(key=str.lower)

with open("sorted.txt", "w") as file:
    file.write("\n".join(words))

print("Words sorted alphabetically")