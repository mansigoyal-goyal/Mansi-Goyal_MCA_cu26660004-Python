with open("file1.txt", "r") as file:
    content1 = file.read()

with open("file2.txt", "r") as file:
    content2 = file.read()

with open("merged.txt", "w") as file:
    file.write(content1 + "\n" + content2)

print("Files merged successfully")