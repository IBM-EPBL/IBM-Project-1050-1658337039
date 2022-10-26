import sqlite3

conn = sqlite3.connect('user_database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE users (name TEXT, email TEXT, password TEXT, confirm_password TEXT)')
print("Table created successfully")
conn.close()