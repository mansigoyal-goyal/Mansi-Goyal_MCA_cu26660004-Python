text = input("Enter a string: ")
substring = input("Enter substring to search: ")

if substring in text:
    print("Substring found.")
else:
    print("Substring not found.")