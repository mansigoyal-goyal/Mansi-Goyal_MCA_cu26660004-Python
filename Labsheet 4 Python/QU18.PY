# Remove a key from dictionary

students = {
    "Mansi": 85,
    "Rahul": 78,
    "Priya": 92
}

key = input("Enter key to remove: ")

if key in students:
    del students[key]
    print("Key removed successfully.")
else:
    print("Key not found.")

print("Dictionary:", students)