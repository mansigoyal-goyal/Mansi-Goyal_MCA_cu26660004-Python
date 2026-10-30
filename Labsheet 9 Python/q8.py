products = {}

# Create
products[101] = {"name": "Laptop", "price": 50000}

# Read
print("Products:", products)

# Update
products[101]["price"] = 48000
print("Updated products:", products)

# Delete
products.pop(101, None)
print("After deletion:", products)