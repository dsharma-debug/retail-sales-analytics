import sqlite3

connection = sqlite3.connect("sales.db")
cursor = connection.cursor()

cursor.execute("""
    SELECT SUM(quantity * unit_price) AS total_revenue
    FROM sales
""")

total_revenue = cursor.fetchone()[0]
cursor.execute("""
    SELECT product, SUM(quantity * unit_price) AS revenue
    FROM sales
    GROUP BY product
    ORDER BY revenue DESC, product ASC
""")

product_revenue = cursor.fetchall()

print("\nProducts ranked by revenue:")
for product, revenue in product_revenue:
    print(f"{product}: ${revenue:.2f}")

cursor.execute("""
    SELECT
        strftime('%Y-%m', date) AS month,
        SUM(quantity * unit_price) AS revenue
    FROM sales
    GROUP BY month
    ORDER BY month
""")

monthly_results = cursor.fetchall()

print("\nMonthly revenue from SQL:")
for month, revenue in monthly_results:
    print(f"{month}: ${revenue:.2f}")
    
connection.close()

print(f"Total revenue from SQL: ${total_revenue:.2f}")
