'''
problem #5
In your college Python is taught in 3 different departments by the same professor. 
For each dept, get the no of students stutying Python and their marks in the final exam 
Get the input as comma seperated string

Find the top 3 marks in each class
Find the top 3 marks if all classes are combined.
Find the avg mark of students with passing mark in each class and the classes combined.
Find which class has the best average mark and least number of failed students.'''

def mark():
    import re
    
    # Input the number of students in each department
    no_of_math_students = int(input("Enter the number of students in the Math department: "))
    no_of_eng_students = int(input("Enter the number of students in the English department: "))
    no_of_phy_students = int(input("Enter the number of students in the Physics department: "))
    
    # Initialize empty dictionaries to store the student data
    math_data = {}
    eng_data = {}
    phy_data = {}
    
    # Input marks for each student in each department
    for i in range(no_of_math_students):
        data = input("Enter data for a Math student (name, marks): ")
        name, marks = re.split(r',\s*', data)
        math_data[name] = float(marks)
    
    for i in range(no_of_eng_students):
        data = input("Enter data for an English student (name, marks): ")
        name, marks = re.split(r',\s*', data)
        eng_data[name] = float(marks)
    
    for i in range(no_of_phy_students):
        data = input("Enter data for a Physics student (name, marks): ")
        name, marks = re.split(r',\s*', data)
        phy_data[name] = float(marks)

    # Find the top 3 marks in each department
    top_3_math = sorted(math_data.values(), reverse=True)[:3]
    top_3_eng = sorted(eng_data.values(), reverse=True)[:3]
    top_3_phy = sorted(phy_data.values(), reverse=True)[:3]

    # Combine all data into one dictionary
    all_data = {**math_data, **eng_data, **phy_data}

    # Find the top 3 marks if all classes are combined
    top_3_combined = sorted(all_data.values(), reverse=True)[:3]

    # Find the average mark of students with passing marks in each class and the classes combined
    pass_mark = 40  # You can adjust this as needed
    math_passing = [marks for marks in math_data.values() if marks >= pass_mark]
    eng_passing = [marks for marks in eng_data.values() if marks >= pass_mark]
    phy_passing = [marks for marks in phy_data.values() if marks >= pass_mark]
    all_passing = [marks for marks in all_data.values() if marks >= pass_mark]

    math_avg_passing = sum(math_passing) / len(math_passing) if len(math_passing) > 0 else 0
    eng_avg_passing = sum(eng_passing) / len(eng_passing) if len(eng_passing) > 0 else 0
    phy_avg_passing = sum(phy_passing) / len(phy_passing) if len(phy_passing) > 0 else 0
    all_avg_passing = sum(all_passing) / len(all_passing) if len(all_passing) > 0 else 0

    # Find which class has the best average mark and the least number of failed students
    best_avg_class = max([(math_avg_passing, 'Math'), (eng_avg_passing, 'English'), (phy_avg_passing, 'Physics')], key=lambda x: x[0])
    failed_students = {
        'Math': no_of_math_students - len(math_passing),
        'English': no_of_eng_students - len(eng_passing),
        'Physics': no_of_phy_students - len(phy_passing),
    }
    least_failed_class = min(failed_students, key=failed_students.get)

    print("Top 3 marks in Math:", top_3_math)
    print("Top 3 marks in English:", top_3_eng)
    print("Top 3 marks in Physics:", top_3_phy)
    print("Top 3 marks if all classes are combined:", top_3_combined)
    print("Average mark in Math (passing students):", math_avg_passing)
    print("Average mark in English (passing students):", eng_avg_passing)
    print("Average mark in Physics (passing students):", phy_avg_passing)
    print("Average mark in all classes (passing students):", all_avg_passing)
    print("Class with the best average mark:", best_avg_class[1])
    print("Class with the least number of failed students:", least_failed_class)

mark()







Regenerate
