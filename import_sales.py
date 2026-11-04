import csv
import sqlite3

connection = sqlite3.connect("sales.db")
cursor = connection.cursor()

with open("sales.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for sale in reader:
        cursor.execute("""
            INSERT OR REPLACE INTO sales
            (sale_id, date, product, category,
             quantity, unit_price, unit_cost)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            int(sale["sale_id"]),
            sale["date"],
            sale["product"],
            sale["category"],
            int(sale["quantity"]),
            float(sale["unit_price"]),
            float(sale["unit_cost"])
        ))

connection.commit()

cursor.execute("SELECT COUNT(*) FROM sales")
record_count = cursor.fetchone()[0]

connection.close()

print(f"Sales records in database: {record_count}")
