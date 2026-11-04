import sqlite3

connection = sqlite3.connect("sales.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        sale_id INTEGER PRIMARY KEY,
        date TEXT NOT NULL,
        product TEXT NOT NULL,
        category TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        unit_price REAL NOT NULL,
        unit_cost REAL NOT NULL
    )
""")

connection.commit()
connection.close()

print("Database and sales table are ready.")
