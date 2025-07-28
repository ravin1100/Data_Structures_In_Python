def display_menu():
    print("\n--- Shopping Cart Menu ---")
    print("1. Add Item")
    print("2. Remove Specific Item")
    print("3. Remove Last Added Item")
    print("4. Display Items in Alphabetical Order")
    print("5. Display Cart Contents with Indices")
    print("6. Exit")

def add_item(cart):
    item = input("Enter item to add: ").strip()
    cart.append(item)
    print(f"'{item}' added to cart.")

def remove_specific_item(cart):
    item = input("Enter item to remove: ").strip()
    if item in cart:
        cart.remove(item)
        print(f"'{item}' removed from cart.")
    else:
        print(f"'{item}' not found in cart.")

def remove_last_item(cart):
    if cart:
        removed_item = cart.pop()
        print(f"Last added item '{removed_item}' removed.")
    else:
        print("Cart is already empty.")

def display_sorted_cart(cart):
    if cart:
        print("Items in alphabetical order:")
        for item in sorted(cart):
            print("-", item)
    else:
        print("Cart is empty.")

def display_cart_with_indices(cart):
    if cart:
        print("Cart contents with indices:")
        for index, item in enumerate(cart):
            print(f"{index}: {item}")
    else:
        print("Cart is empty.")

def shopping_cart_app():
    cart = []
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == "1":
            add_item(cart)
        elif choice == "2":
            remove_specific_item(cart)
        elif choice == "3":
            remove_last_item(cart)
        elif choice == "4":
            display_sorted_cart(cart)
        elif choice == "5":
            display_cart_with_indices(cart)
        elif choice == "6":
            print("Exiting Shopping Cart. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the application
shopping_cart_app()
