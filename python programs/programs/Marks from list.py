'''
Problem #2
you have a list of student names and another list with their marks in CS. 
hard code the values. no need to get it as input
Pass mark is 50.
Print a new list with all the students with pass marks along with their mark in the format name:mark.
Also print the number of students who failed.


'''
pass_students = []
student_names = ["chithra","ram","kaviya","nithya","rathna"]

marks = [90,45,36,70,80]
 
for i , mark in enumerate(marks):
    if mark>=50:
        pass_students.append(student_names[i])
print("the names of the students who are passed in cs is",pass_students)



 