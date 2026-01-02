# Experiment 4: File Handling and Exception Handling

filename = "attendance.txt"

try:
    # Writing student data to file
    with open(filename, "w") as file:
        student_id = input("Enter Student ID: ")
        student_name = input("Enter Student Name: ")
        attendance = input("Enter Attendance (Present/Absent): ")

        file.write("Student ID: " + student_id + "\n")
        file.write("Student Name: " + student_name + "\n")
        file.write("Attendance: " + attendance + "\n")

    print("\nData written to file successfully.")

    # Reading data from file
    print("\n--- File Contents ---")
    with open(filename, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Error: File not found.")

except Exception as e:
    print("Error:", e)
