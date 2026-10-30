def read_records():
    try:
        with open("records.txt", "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []

def save_records(records):
    with open("records.txt", "w") as file:
        for record in records:
            file.write(record + "\n")

records = read_records()

# Create
records.append("1,Aman,85")
save_records(records)

# Read
print("Records:", read_records())

# Update
records = read_records()
records = [
    "1,Aman,90" if r.startswith("1,") else r
    for r in records
]
save_records(records)

# Delete
records = [r for r in read_records() if not r.startswith("1,")]
save_records(records)

print("Final records:", read_records())