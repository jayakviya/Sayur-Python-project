mark1 = int(input("Enter the mark in subject 1 :"))
mark2 = int(input("Enter the mark in subject 2 :"))
mark3 = int(input("Enter the mark in subject 3 :"))
if (mark1 == 100) or (mark2 == 100) or (mark3 == 100):
# if student has mark 100 in anyone subject 
    print("A Grade")
elif (mark1 >= 90) or (mark2 >= 90) or (mark3 >= 90):
# if student has 90 or above in anyone subject
    print("B Grade")
elif (mark1 >= 60) or (mark2 >= 60) or (mark3 >= 60):
# if student has 60 or above in anyone subject
    print("C Grade")
elif (mark1 <= 50) and (mark2 <= 50) and (mark3 <= 50):
#if student has 50 or less than in all subjects 
    print("F Grade")
else:
    print("D Grade")
