import csv

with open("sales.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    sales = list(reader)

print("Retail Sales Analytics")
print("Number of sales records:", len(sales))

print("\nFirst three sales:")
for sale in sales[:3]:
    print(sale["date"], "-", sale["product"], "-", sale["quantity"])

total_revenue = 0.0

for sale in sales:
    quantity = int(sale["quantity"])
    unit_price = float(sale["unit_price"])

    revenue = quantity * unit_price
    total_revenue += revenue

print(f"\nTotal revenue: ${total_revenue:.2f}")

total_cost = 0.0

for sale in sales:
    quantity = int(sale["quantity"])
    unit_cost = float(sale["unit_cost"])

    total_cost += quantity * unit_cost

gross_profit = total_revenue - total_cost

print(f"Total product cost: ${total_cost:.2f}")
print(f"Gross profit: ${gross_profit:.2f}")

product_units = {}

for sale in sales:
    product = sale["product"]
    quantity = int(sale["quantity"])

    product_units[product] = product_units.get(product, 0) + quantity

print("\nUnits sold by product:")
for product, quantity in product_units.items():
    print(f"{product}: {quantity}")

best_seller = max(product_units, key=product_units.get)

print(f"\nBest-selling product: {best_seller}")
print(f"Units sold: {product_units[best_seller]}")

monthly_revenue = {}

for sale in sales:
    month = sale["date"][:7]
    quantity = int(sale["quantity"])
    unit_price = float(sale["unit_price"])

    revenue = quantity * unit_price
    monthly_revenue[month] = monthly_revenue.get(month, 0) + revenue

print("\nRevenue by month:")
for month in sorted(monthly_revenue):
    print(f"{month}: ${monthly_revenue[month]:.2f}")


with open("sales_report.txt", "w", encoding="utf-8") as report:
    report.write("RETAIL SALES ANALYTICS\n")
    report.write("Dataset: fictional practice sales\n\n")

    report.write(f"Sales records: {len(sales)}\n")
    report.write(f"Total revenue: ${total_revenue:.2f}\n")
    report.write(f"Total product cost: ${total_cost:.2f}\n")
    report.write(f"Gross profit: ${gross_profit:.2f}\n")

    report.write(f"\nBest-selling product: {best_seller}\n")
    report.write(f"Units sold: {product_units[best_seller]}\n")

    report.write("\nRevenue by month:\n")
    for month in sorted(monthly_revenue):
        report.write(f"{month}: ${monthly_revenue[month]:.2f}\n")

print("\nReport saved to sales_report.txt")
