# main.py

import grade_module

marks1 = int(input("Enter marks of Student 1: "))
marks2 = int(input("Enter marks of Student 2: "))

print("Student 1:", grade_module.calculate_grade(marks1))
print("Student 2:", grade_module.calculate_grade(marks2))
