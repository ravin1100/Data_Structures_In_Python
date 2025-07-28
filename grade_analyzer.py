# Given the list grades = [85, 92, 78, 90, 88, 76, 94, 89, 87, 91], perform the following operations:

# Slice grades from index 2 to 7
# Use list comprehension to find grades above 85
# Replace the grade at index 3 with 95
# Append three new grades
# Sort in descending order and display the top 5 grades

grades = [85, 92, 78, 90, 88, 76, 94, 89, 87, 91]

print(grades[2:7])

print([grade for grade in grades if grade > 85])

grades[3] = 95
print(grades)

# grades.append(20)
# grades.append(30)
# grades.append(40)
# print(grades)

new_grades = [20,30,40]
grades.extend(new_grades)
print(grades)


print(sorted(grades, reverse=True)[:5])