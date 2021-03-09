import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully");

conn.execute("DROP TABLE IF EXISTS appointments")
print("Table successfully dropped");

conn.execute('CREATE TABLE appointments (year INT, month INT, day INT, slot INT)')
print("Table created successfully");

conn.commit()

conn.close()
