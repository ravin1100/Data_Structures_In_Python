# Tasks:
# Create Product-Price Pairs
# Use zip() to pair each product with its corresponding price.

# Calculate Total Value for Each Product
# For each product, calculate the total inventory value using the formula: price × quantity.

# Build a Product Catalog Dictionary
# Create a dictionary where each product maps to another dictionary containing its price and quantity.

# Find Low Stock Products
# Identify and print the names of products with a quantity less than 10.


products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [999.99, 25.50, 75.00, 299.99]
quantities = [5, 20, 15, 8]

print(list(zip(products, prices)))

for index, product in enumerate(products):
    print(f"{product}: {prices[index]*quantities[index]}")

dictionary = {product:{"price":price, 'quantity':quantity} for product, price, quantity in zip(products, prices, quantities)}

print(dictionary)


for index, product in enumerate(products):
    if quantities[index] < 10:
        print(product, end=" ")