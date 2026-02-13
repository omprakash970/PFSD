class Student: 
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self._marks = marks #private variable
    def get_marks(self):
        return self._marks
    def set_marks(self, marks):
        if marks>=0:
            self._marks = marks
    def display_details(self):
        print(f'Student ID: {self.student_id}, Name: {self.name}, Marks: {self._marks}')

class GraduateStudent(Student): 
    def __init__(self, student_id, name, marks, specialization): 
        super().__init__(student_id, name, marks)
        self.specialization = specialization
    def display_details(self):
        super().display_details()
        print(f'Specialization: {self.specialization}')

student1 = Student(101, "Alice", 85)
student2 = GraduateStudent(102, "Bob", 90, "Computer Science")
student1.display_details()
print()
student2.display_details()
