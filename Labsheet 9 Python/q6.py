employees = {}

# Create
employees[101] = {"name": "Aman", "salary": 25000}

# Read
print("Employees:", employees)

# Update
employees[101]["salary"] = 30000
print("Updated:", employees)

# Delete
employees.pop(101, None)
print("After deletion:", employees)