# 3. Accept 2 integers. print all nos which are mirror nos falling 
# between the range.
# eg: first no 300
#  second no 400
# 303,313,323.......393
num1 = int(input("Enter the first integer:"))
num2 = int(input("Enter the second integer:"))
mirrer_numbers = []
for num in range(num1,num2+1):
    
    if str(num)== str(num)[::-1]:

        mirrer_numbers.append(num)

print("The mirres numbers are,",mirrer_numbers)

'''
output:
Enter the first integer:400
Enter the second integer:500
The mirres numbers are, [404, 414, 424, 434, 444, 454, 464, 474, 484, 494]'''