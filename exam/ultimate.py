def write_attendence():
    try:
        n=int(input("Enter the no.of students"))
        if n<=0:
            raise ValueError
        with open("attendance.txt", "w") as file:
            for i in range(n):
                name=input(f"Enter the name of the student")
                status=input(f"Present or Absent(P/A)")
                file.write(f"{name}-{status}")
    except ValueError:
        print("Enter some +ve number")
    except Exception as e:
        print(f"An error occurred: {e}")
def read_attendence():
    try: 
        with open("attandance.txt", "r")as file:
            for line in file: 
                print(line.strip())
    except FileNotFoundError:
        print("404 error not found")
    except Exception as e: 
        print(f"An error occurred : {e}")
