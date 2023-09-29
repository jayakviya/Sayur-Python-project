
# '''Write a program for Collatz_conjecture.
# # Collatz_conjecture means -  start with the input number. 
# # For even number , divide by 2 (n/2)
# # For odd number - 3n + 1
# # apply the above for the result number until the answer is 1.'''


# num1 = int(input("Enter your number 1"))
# num2 = int(input("Enter your number 2"))
# count1 = 0
# count2 = 0
# while num1!= 1:

#     if num1% 2 == 0 :
#         num1= int(num1/2)
#     else :
#         num1 = (3*num1)+1
#     count1+=1
# print("The resuut value is 1 after the no of iterations",count1 )
# while num2!= 0:
#     if num2% 2 == 0 :
#          num2= int(num2/2)
#      else :
#          num2 = (3*num2)+1
#      count2+=1
#  if count1 < count2:
#      print(f"The resuut value of both munber is 1 after the no of iterations for the {num1} is {count1} is less than no of iterations for the n{num2} is {count2} ")


# '''
# output 1:
# Enter your number56
# The resuut value  1
# output 2:
# Enter your number56
# The resuut value  1'''
num =[]
count = []
for i in range (2):
    num = int(input("Enter the num",i+1))
for n in num:
    while n != 0:
        if n %2==0:
            n = n//2
        else:
            n= 3*n +1
    count[n.index()]+=1
minCount = min(count)
print(f"The result is 1 after no of interations of {num[minCount.index]}")


