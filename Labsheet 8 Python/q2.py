import sqlite3

conn = sqlite3.connect("college.db")
print("Database created successfully")
conn.close()