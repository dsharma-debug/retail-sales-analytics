import sqlite3
from html import escape

connection = sqlite3.connect("sales.db")
cursor = connection.cursor()

cursor.execute("""
    SELECT
        strftime('%Y-%m', date) AS month,
        SUM(quantity * unit_price) AS revenue
    FROM sales
    GROUP BY month
    ORDER BY month
""")

monthly_results = cursor.fetchall()

print("Monthly revenue:")
for month, revenue in monthly_results:
    print(f"{month}: ${revenue:.2f}")

cursor.execute("""
    SELECT
        SUM(quantity * unit_price),
        SUM(quantity * unit_cost)
    FROM sales
""")

total_revenue, total_cost = cursor.fetchone()
gross_profit = total_revenue - total_cost

cursor.execute("""
    SELECT
        product,
        SUM(quantity) AS units,
        SUM(quantity * unit_price) AS revenue,
        SUM(quantity * (unit_price - unit_cost)) AS gross_profit
    FROM sales
    GROUP BY product
    ORDER BY revenue DESC, product ASC
""")

product_results = cursor.fetchall()

print("\nProduct performance:")
for product, units, revenue, profit in product_results:
    print(
        f"{product}: {units} units | "
        f"Revenue ${revenue:.2f} | Gross profit ${profit:.2f}"
    )

connection.close()

max_revenue = max(revenue for month, revenue in monthly_results)
monthly_bars = ""

for month, revenue in monthly_results:
    width = revenue / max_revenue * 100

    monthly_bars += f"""
    <div class="bar-row">
        <p>{month}: ${revenue:.2f}</p>
        <div class="bar-track" aria-hidden="true">
            <div class="bar-fill" style="width: {width:.1f}%;"></div>
        </div>
    </div>
    """

product_rows = ""

for product, units, revenue, profit in product_results:
    product_rows += f"""
    <tr>
        <td>{escape(product)}</td>
        <td>{units}</td>
        <td>${revenue:.2f}</td>
        <td>${profit:.2f}</td>
    </tr>
    """

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Retail Sales Dashboard</title>
    <link rel="stylesheet" href="dashboard.css">
</head>
<body>
    <h1>Retail Sales Dashboard</h1>
    <p>Data source: fictional practice sales.</p>

    <div class="metrics">
        <div class="card">
            <h2>Total revenue</h2>
            <p>${total_revenue:.2f}</p>
        </div>

        <div class="card">
            <h2>Product costs</h2>
            <p>${total_cost:.2f}</p>
        </div>

        <div class="card">
            <h2>Gross profit</h2>
            <p>${gross_profit:.2f}</p>
        </div>
    </div>
<section class="chart">
    <h2>Monthly revenue (USD)</h2>
    {monthly_bars}
</section>    

<section class="chart">
    <h2>Product performance</h2>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>Product</th>
                    <th>Units sold</th>
                    <th>Revenue</th>
                    <th>Gross profit</th>
                </tr>
            </thead>
            <tbody>
                {product_rows}
            </tbody>
        </table>
    </div>
</section>

</body>
</html>
"""

with open("dashboard.html", "w", encoding="utf-8") as file:
    file.write(page)

print("Dashboard saved to dashboard.html")
