# Tasks:
# Print Teacher Names
# Iterate through all classes and print the name of each teacher.

# Calculate Class Average Grades
# For each class, calculate and display the average grade of the students.

# Find Top Student Across All Classes
# Identify the student with the highest grade among all students across every class.

# Use Unpacking
# Use tuple unpacking to extract and work with student names and grades separately.


school = {
    "Math": {
        "teacher": "Mr. Smith",
        "students": [("Alice", 85), ("Bob", 92), ("Carol", 78)]
    },
    "Science": {
        "teacher": "Ms. Johnson",
        "students": [("David", 88), ("Eve", 94), ("Frank", 82)
        ]
    }
}

# print([value['teacher'] for key, value in school.items()])

for key, value in school.items():
    print(f"{key}: {value['teacher']}")

for key, value in school.items():
    sum = 0
    students = value['students']
    for s in students:
        sum+= s[1]
    print(f"AVG of {key}: {sum/len(students)}")


for key, value in school.items():
    # print(max(score for name, score in value['students']))
    print(sorted(value['students'], key = lambda x : x[1], reverse=True)[0])

top_student  = ("", 0)

for key, value in school.items():
    for name, grade in value['students']:
        if grade > top_student[1]:
            top_student = (name, grade)
    
print(f"topper is: \n{top_student[0]} with grade {top_student[1]}")

for key, value in school.items():
    for name, grade in value['students']:
        print(f"name: {name}, grade: {grade}")

