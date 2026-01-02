# Experiment 1: Python Basics

# 1. Read a number from the user
num = int(input("Enter a number: "))

# 2. Check whether the number is positive, negative, or zero
if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

print("\n--- Student Details ---")

# 3. Create variables for student details
student_id = 1024              # int
student_name = "Om Prakash"    # str
marks = 92.5                   # float
attendance_status = True       # bool

# 4. Display value and data type of each variable
print("Student ID:", student_id, "| Data Type:", type(student_id))
print("Student Name:", student_name, "| Data Type:", type(student_name))
print("Marks:", marks, "| Data Type:", type(marks))
print("Attendance Status:", attendance_status, "| Data Type:", type(attendance_status))

print("\n--- Arithmetic Operations ---")

# 5. Arithmetic operations
a = 20
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
