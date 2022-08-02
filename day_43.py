# Day 43: Student Marks
# Write a function called student_marks that records marks achieved
# by students in a test. The function should ask the user to input the
# name of the student and then ask the user to input the marks
# achieved by the student. The information should be stored in a
# dictionary. The name is the key and the marks are the value. When
# the user enters done, the function should return a dictionary of
# names and values entered.

grades = dict()
count = 3

def student_marks():
    name = None
    while True:
        d = dict()
        name = input("Enter the Student's name : ")
        if name == 'done': break
        mark = input("Enter the student's mark : ")
        d = {name : mark}
        grades.update(d)
    return grades

print(student_marks())    
        
