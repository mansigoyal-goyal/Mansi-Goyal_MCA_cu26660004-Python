import csv

files = ["students1.csv", "students2.csv"]

with open("combined.csv", "w", newline="") as output:
    writer = csv.writer(output)

    for index, filename in enumerate(files):
        with open(filename, "r", newline="") as source:
            reader = csv.reader(source)

            for row_number, row in enumerate(reader):
                # Write the header only once
                if index == 0 or row_number > 0:
                    writer.writerow(row)

print("CSV files combined successfully")