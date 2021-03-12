import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully");

conn.execute("DROP TABLE IF EXISTS appointments")
conn.execute("DROP TABLE IF EXISTS persons")
print("Table successfully dropped");

conn.execute('CREATE TABLE appointments (year INT, month INT, day INT, slot INT, p_id INT)')
print("Table appointments created successfully");

conn.execute('CREATE TABLE persons (id INT, firstname TEXT, lastname TEXT, insuranceID TEXT)')
print("Table persons created successfully");

conn.execute("INSERT INTO persons (id, firstname, lastname, insuranceID) VALUES (?, ?, ?, ?)", (0, "P1firstname", "P1lastname", "P1id"))
conn.execute("INSERT INTO persons (id, firstname, lastname, insuranceID) VALUES (?, ?, ?, ?)", (1, "P4firstname", "P4lastname", "P4id"))
conn.execute("INSERT INTO persons (id, firstname, lastname, insuranceID) VALUES (?, ?, ?, ?)", (2, "P3firstname", "P3lastname", "P3id"))
conn.execute("INSERT INTO persons (id, firstname, lastname, insuranceID) VALUES (?, ?, ?, ?)", (3, "P2firstname", "P2lastname", "P2id"))
print("Table persons filled successfully");

conn.commit()

conn.close()
