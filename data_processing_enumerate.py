# Tasks:
# Create a Numbered List of Students
# Print each student’s name with a number starting from 1 (e.g., 1. Alice).

# Pair Students with Their Scores Using enumerate()
# Combine both lists to display each student's name alongside their score.

# Find Positions of High Scorers
# Identify and print the positions (indices) of students who scored above 90.

# Map Positions to Student Names
# Create a dictionary where keys are positions (starting from 0) and values are the student names.



students = ["Alice", "Bob", "Carol", "David", "Eve"]
scores = [85, 92, 78, 88, 95]

for i, s in enumerate(students, start=1):
    print(f"{i}. {s}")

for i, s in enumerate(students):
    print(f"{s}: {scores[i]}")

for i, s in enumerate(students):
    if scores[i]>90:
        print(f"{i}, {s}")

dictioary = {i: name for i, name in enumerate(students)}
print(dictioary)








