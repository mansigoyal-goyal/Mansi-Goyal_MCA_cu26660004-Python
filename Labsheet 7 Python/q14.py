with open("sample.txt", "r") as file:
    lines = file.readlines()

if lines:
    longest = max(lines, key=len)
    print("Longest line:", longest.strip())
else:
    print("File is empty")