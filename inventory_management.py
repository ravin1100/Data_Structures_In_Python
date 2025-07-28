# Tasks:
# Add a New Product
# Add a new product to the inventory with its price and quantity.

# Update Product Price
# Update the price of an existing product (e.g., change the price of "bananas").

# Sell 25 Apples
# Simulate the sale of 25 apples by updating the quantity accordingly.

# Calculate Total Inventory Value
# Compute the total value of the inventory using the formula:
# total = sum(price × quantity for all products)

# Find Low Stock Products
# Identify and print all products whose quantity is below 100.


inventory = {
    "apples": {"price": 1.50, "quantity": 100},
    "bananas": {"price": 0.75, "quantity": 150},
    "oranges": {"price": 2.00, "quantity": 80}
}

inventory["papaya"] = {"price":3.00, "quantity":200}

print(inventory)

inventory["bananas"]["price"] = 0.85

print(inventory)

inventory["apples"]["quantity"] = inventory["apples"]["quantity"] - 25
print(inventory)


print(sum(item['price']*item['quantity'] for item in inventory.values()))

for key, value in inventory.items():
    if value['quantity'] < 100:
        print(f"{key}: {value['quantity']}")

