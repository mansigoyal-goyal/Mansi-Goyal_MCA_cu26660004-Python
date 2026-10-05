# Check whether a key exists

students = {
    "Mansi": 85,
    "Rahul": 78,
    "Priya": 92
}

key = input("Enter key to search: ")

if key in students:
    print("Key exists in the dictionary.")
else:
    print("Key does not exist.")