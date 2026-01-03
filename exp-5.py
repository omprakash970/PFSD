# Experiment 5: Object-Oriented Programming in Python

# Base class
class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id     
        self.__marks = marks              # private (encapsulation)

    def get_marks(self):
        return self.__marks

    def display_details(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Marks:", self.get_marks())


# Derived class (Inheritance)
class GraduateStudent(Student):
    def __init__(self, student_id, name, marks, specialization):
        super().__init__(student_id, name, marks)
        self.specialization = specialization
        
    def display_details(self):
        super().display_details()
        print("Specialization:", self.specialization)


student1 = Student(101, "Om Prakash", 88)
student2 = GraduateStudent(201, "Rahul", 92, "Computer Science")

print("\n--- Student Details ---")
student1.display_details()

print("\n--- Graduate Student Details ---")
student2.display_details()
