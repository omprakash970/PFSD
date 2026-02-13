def write_attendance():
    try: 
        n=int(input("Enter the number of students: "))
        if n<=0:
            raise ValueError
        with open("attendance.txt", "w") as file: 
            for i in range(n):
                name=input(f"Enter the name: \n")
                status=input(f"Enter the attendance status(Present/Absent)\n")
                file.write(f"{name}:{status}\n")
        print("Attendance recorded successfully.")
    except ValueError:
        print("Invalid input. Please enter a positive integer for the number of students.")
    except Exception as e:
        print(f"An error occurred: {e}")
def read_attendance(): 
    try:
        with open("attendance.txt", "r") as file: 
            print("Attendance List:")
            for line in file: 
                print(line.strip())
    except FileNotFoundError:
        print("Attendance file not found. Please record attendance first.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    write_attendance()
    read_attendance()