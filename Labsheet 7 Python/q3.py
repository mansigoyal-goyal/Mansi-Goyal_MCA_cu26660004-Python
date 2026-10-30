# Create a file containing multiple lines
with open("sample.txt", "w") as file:
    file.write("Apple\n")
    file.write("Banana\n")
    file.write("Mango\n")

# Read and display each line
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())