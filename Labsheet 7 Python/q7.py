with open("user_data.txt", "w") as file:
    while True:
        line = input("Enter text (type stop to finish): ")

        if line.lower() == "stop":
            break

        file.write(line + "\n")

print("Data saved successfully")