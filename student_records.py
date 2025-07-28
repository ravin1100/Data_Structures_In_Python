# Tasks:
# Find the Student with the Highest Grade
# Identify and print the student who has the highest grade from the list.
# Create a Name-Grade List
# Generate a new list containing only the name and grade of each student in the format: ("Alice", 85).
# Demonstrate Tuple Immutability
# Attempt to change the grade of a student in the original list and show why this is not allowed with tuples. Explain briefly why tuples are preferred for immutable records like student data.

# (student_id, name, grade, age)

students = [
    (101, "Alice", 85, 20),
    (102, "Bob", 92, 19),
    (103, "Carol", 78, 21),
    (104, "David", 88, 20)
]


print(max(students, key = lambda x: x[2]))

name_grade_list = [(s[1], s[2]) for s in students]
print(name_grade_list)

students[0][2] = 95  #TypeError: 'tuple' object does not support item assignment
print(students[0])  



