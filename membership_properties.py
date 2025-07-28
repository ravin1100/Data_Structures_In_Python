# Different data structures to store fruits
fruits_list = ["apple", "banana", "orange", "apple", "grape"]  # List allows duplicates
fruits_tuple = ("apple", "banana", "orange")                   # Tuple is immutable
fruits_set = {"apple", "banana", "orange", "grape"}            # Set removes duplicates
fruits_dict = {"apple": 5, "banana": 3, "orange": 8, "grape": 2}  # Dict maps fruits to quantities


# Tasks:
# Check for Membership
# Test whether "apple" is present in each data structure.

# Find Length
# Display the number of elements in each structure using len().

# Iterate and Print Elements
# Loop through each structure and print its contents.

# Compare Membership Testing Performance
# Briefly explain which data structures are more efficient for membership checks and why.

# Demonstrate Different Iteration Patterns
# Use appropriate iteration patterns (e.g., for item in set, for key in dict, etc.) to traverse each structure effectively.


def membership_check(fruit_name):
    if fruit_name in fruits_list:
        print(f"{fruit_name} is present in fruits_list")
    if fruit_name in fruits_tuple:
        print(f"{fruit_name} is present in fruits_tuple")
    if fruit_name in fruits_set:
        print(f"{fruit_name} is present in fruits_set")
    if fruit_name in fruits_dict:
        print(f"{fruit_name} is present in fruits_dict")

membership_check("apple")

print(f"Length of list: {len(fruits_list)}")
print(f"Length of tuple: {len(fruits_tuple)}")
print(f"Length of set: {len(fruits_set)}")
print(f"Length of dictionary: {len(fruits_dict)}")


for fruit in fruits_list:
    print(f"{fruit}", end=" ")
print()

for fruit in fruits_tuple:
    print(f"{fruit}", end=" ")
print()

for fruit in fruits_set:
    print(f"{fruit}", end=" ")
print()

for fruit in fruits_dict:
    print(f"Fruit: {fruit}, Quantity: {fruits_dict[fruit]}", end="\n")
print()

for key, value in fruits_dict.items():
    print(f"{key} -> {value}")
    
