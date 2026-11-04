# Retail Sales Analytics

A practice data analysis project using Python, SQL, and SQLite.
It turns sales records into a text report and a browser dashboard.

## Dataset

The included dataset contains 12 fictional sales records covering
January through March 2026. Each record includes a product,
category, quantity, selling price, and unit cost.

All findings describe this fictional practice dataset.

## Features

- Calculate revenue, product costs, and gross profit.
- Identify the best-selling product by units.
- Rank products by revenue.
- Compare monthly revenue.
- Display summary cards, a revenue chart, and a product table.
- Rebuild the outputs with one command.

Gross profit excludes expenses such as rent, wages, and utilities.

## Tools

- Python: CSV processing and workflow automation.
- SQL and SQLite: data storage and analysis.
- HTML and CSS: dashboard presentation.

The Python scripts use the standard library.

## How to run

1. Install Python 3.
2. Download the project and open its folder in a terminal.
3. Run:

```bash
python3 run_project.py
```

4. Open dashboard.html in a browser.
5. Open sales_report.txt to read the text report.

## Updating the data

Edit quantities or prices in sales.csv, or add records with new,
unique sale IDs. Run the project again and refresh the dashboard.

The import updates existing sale IDs and adds new ones.

## Example findings

- Total revenue: $269.00.
- Gross profit: $94.80.
- Apples had the most units sold: 25.
- Bread and Milk each generated $72.00 in revenue.
- Monthly revenue increased from $75.00 in January
  to $101.50 in March.

## Workflow

CSV data → SQLite database → SQL analysis → report and dashboard.