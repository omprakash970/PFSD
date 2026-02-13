import grading_module as gm
marks_list= [95, 85, 76, 65, 55]
for marks in marks_list: 
    grade = gm.calculate_grade(marks)
    print(f'Marks: {marks}, Grade: {grade}')