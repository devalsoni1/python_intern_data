# import csv
# data = [
# ["name", "address", "mobile", "email"],
# ["Alice Johnson", "123 Main St, Springfield", "9876543210", "alice@example.com"],
# ["Bob Smith", "456 Oak Ave, Metropolis", "9123456789", "bob@example.com"],
# ["Carol Lee", "789 Pine Rd, Gotham", "9988776655", "carol@example.com"]
# ]

# with open("address_book.csv","w",newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# print("csv file crated succesjack")

# import csv

# weather_data= {
#     "city": "Delhi",
#     "temp": "35",
#     "humi": "0"
# }

# # print(f"weather is {weather_data['city']}")
# with open("weather_data.csv","w",newline="")as file:
#     writer = csv.writer(file)

#     writer.writerow(weather_data.keys())
#     writer.writerow(weather_data.values())

# print("Weather data saved to CSV")

# import sqlite3

# # Connect to a new SQLite database (creates file if not exists)
# conn = sqlite3.connect("sqlite.db")

# # Create table
# conn.execute('''
# CREATE TABLE IF NOT EXISTS student (
#     st_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     st_nm VARCHAR(50),
#     st_class VARCHAR(20),
#     st_email VARCHAR(80)
# )
# ''')

# # Close connection
# conn.close()

# print("Table created successfully!")

# import sqlite3

# # Connect to database
# conn = sqlite3.connect("sqlite.db")

# # SQL statement
# ins = '''
# INSERT INTO student (st_nm, st_class, st_email)
# VALUES (?, ?, ?)
# '''

# # Multiple records
# data = [
#     ("abc", "12", "abc@gmail.com"),
#     ("xyz", "11", "xyz@gmail.com"),
#     ("pqr", "10", "pqr@gmail.com")
# ]

# # Insert many rows
# conn.executemany(ins, data)

# # Save changes
# conn.commit()
# conn.close()

# import sqlite3

# conn = sqlite3.connect("sqlite.db")

# data = conn.execute("SELECT * FROM student ORDER BY st_nm DESC")

# for m in data:
#     print(m)

# id = input("name to delete:")

# conn.execute("DELETE FROM student WHERE name=" + id)

# conn.commit()

# data1 = conn.execute("SELECT * FROM student ORDER BY st_nm DESC")

# for m in data1:
#     print(m)

# conn.close()

import sqlite3

# 1. Connect to a new database file (or create it if it doesn't exist)
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# 2. Create 2 tables: customers, orders
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    product TEXT,
    amount REAL,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
)
""")

print("Tables created successfully.")

# 3. Insert some records
cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))
cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", ("Bob", "bob@example.com"))

cursor.execute("INSERT INTO orders (customer_id, product, amount) VALUES (?, ?, ?)", (1, "Laptop", 1200.50))
cursor.execute("INSERT INTO orders (customer_id, product, amount) VALUES (?, ?, ?)", (2, "Phone", 650.75))

conn.commit()
print("Records inserted successfully.")

# 4. Perform different SELECT operations
print("\nAll customers:")
for row in cursor.execute("SELECT * FROM customers"):
    print(row)

print("\nOrders where amount > 700:")
for row in cursor.execute("SELECT * FROM orders WHERE amount > 700"):
    print(row)

print("\nJoin customers and orders:")
query = """
SELECT customers.name, orders.product, orders.amount
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
"""
for row in cursor.execute(query):
    print(row)

# 5. Update some data
cursor.execute("UPDATE customers SET email = ? WHERE name = ?", ("alice_new@example.com", "Alice"))
conn.commit()
print("\nUpdated Alice's email.")

# Verify update
cursor.execute("SELECT * FROM customers WHERE name = ?", ("Alice",))
print(cursor.fetchone())

# 6. Delete some data
cursor.execute("DELETE FROM orders WHERE product = ?", ("Phone",))
conn.commit()
print("\nDeleted order for Phone.")

# Verify delete
print("\nRemaining orders:")
for row in cursor.execute("SELECT * FROM orders"):
    print(row)

# Close connection
conn.close()


