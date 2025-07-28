
# Tasks:
# Calculate Total Sales per Quarter
# Use unpacking to compute and display the total sales for each quarter.

# Find the Month with Highest Sales
# Identify the month with the highest individual sales across all quarters.

# Create a Flat List of Monthly Sales
# Generate a flat list of all monthly sales in the format: ("Jan", 1000), ("Feb", 1200), ....

# Use Unpacking in Loops
# Use tuple unpacking while iterating to clearly separate months, sales values, and quarters.

sales_data = [
    ("Q1", [("Jan", 1000), ("Feb", 1200), ("Mar", 1100)]),
    ("Q2", [("Apr", 1300), ("May", 1250), ("Jun", 1400)]),
    ("Q3", [("Jul", 1350), ("Aug", 1450), ("Sep", 1300)])
]

for key, value in sales_data:
    print(sum(sale for _ , sale in value))

print()

month_data = max(sale for _, sale in value for _, value in sales_data)
print(month_data)

print()

monthly_sales = [(month, sale) for month, sale in value for key, value in sales_data]
print(monthly_sales)

for key, value in sales_data:
    for month, sale in value:
        print(f"Quarter: {key}, Month: {month}, Sale: {sale}")