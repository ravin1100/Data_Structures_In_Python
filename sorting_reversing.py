
# Tasks:
# Sort by Salary
# Sort the list of employees by salary in both ascending and descending order.

# Sort by Department, Then by Salary
# First sort by department name alphabetically, then by salary within each department.

# Create a Reversed List
# Reverse the order of the original list of employees without modifying the original.

# Sort by Name Length
# Sort employees based on the length of their names.

# Use sorted() vs .sort() Appropriately
# Use .sort() when modifying the original list and sorted() when creating a new sorted list. Demonstrate both methods.

employees = [
    ("Alice", 50000, "Engineering"),
    ("Bob", 60000, "Marketing"),
    ("Carol", 55000, "Engineering"),
    ("David", 45000, "Sales")
]

print(sorted(employees, key=lambda x: x[1]))
print(sorted(employees, key=lambda x: x[1], reverse=True))

print(sorted(employees, key=lambda x: (x[2], x[1])))
print()
print(employees[::-1])
print()
print(employees)
print()
print(sorted(employees, key=lambda x: len(x[0])))
print()
employees.sort(key = lambda x: x[1])
print(employees)






