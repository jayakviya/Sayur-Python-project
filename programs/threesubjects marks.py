'''
Problem #3
you have a list of student names. you have one list each for their marks in CS, Math and English. 
hard code the values. no need to get it as input
Pass mark is 50.
Grade A is, mark 90 or above
Grade B , 80 or above
Fail is < 50
Print the name of the students who got A in all subjects or atleast one A and the rest B.
Try to use only one if statement.
'''

student_name = ['parthiban','govind','sara','shiva']
cs_mark = [79,89,54,100]
math_mark = [98,83,88,67]
eng_mark = [74,91,100,100]
pass_stu = []
for i in range(len(cs_mark)):
    if (cs_mark[i]>= 90 or math_mark[i]>= 90 or eng_mark[i]>= 90) and (cs_mark[i]>= 80 and math_mark[i]>= 80 and eng_mark[i]>= 80):
        pass_stu.append(student_name[i])
print(pass_stu)

'''
output 
['govind']
'''


