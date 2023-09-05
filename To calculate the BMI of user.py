#To calculate the BMI of user and tell him/her 
# print he/she is overweight/underweight/normal/obuse according to their weight
weight = int(input("Enter your weight = "))
height = int(input("Enter your height = "))
height1 = height/100
bmi = weight/(height1*height1)
print(bmi)
if bmi >= 30:
    print("You are obese You must take care of you health")
elif 25 <= bmi < 29.9:
    print("You are overwaight")
elif 18.5 <= bmi < 24.9:
    print("You are within the normal weight range")
else:
    print("You are underweight you should take care of yourself")
 

