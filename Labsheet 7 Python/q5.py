with open("sample.txt", "r") as file:
    content = file.read()

# Count lines and characters
lines = content.splitlines()
characters = len(content)

print("Number of lines:", len(lines))
print("Number of characters:", characters)