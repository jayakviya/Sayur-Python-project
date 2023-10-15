'''
String manipulation exercises. Use builtin functions as needed.

1. Print the level of the password security and if the password is acceptable
    Weak - only alphabets or only numbers or only special chars
    Ok - at least one alphabet, one number and one special char
    strong - at least three alphabets, two numbers and one special char
    Very strong - same as strong, but at least 16 count

    All passwords must be at least 8 chars long. You can use RegEx if you want.

'''

import re
password = input("Create your password :")#to get the input
noOfAlphas = re.findall(r'[a-zA-Z]',password)#To seperate the alphabets
noOfNums = re.findall(r'[0-9]',password)#To seperate the numbers
noOfSpls = re.findall(r'[^a-zA-Z0-9]',password)#To seperate the special characters
#to check the lenght of the password is more than 8
if len(password) >= 8:
    if len(noOfAlphas)==len(password) or len(noOfNums)==len(password) or len(noOfSpls)==len(password):
        #To check if all charactersis of one category
        print("Your password is weak, it contains only alphabets or only numbers or only special chars")
    elif len(noOfAlphas)>=3 and len(noOfNums)>=2 and len(noOfSpls)>=1:
    
        if len(password)>=16:
            print("Your password is very strong ,it contains 16 count")
        else:
            print("Your password is strong, it contains at least three alphabets, two numbers and one special char")
    elif len(noOfAlphas)>=1 and len(noOfNums)>=1 and len(noOfSpls)>=1:
        print("Your password is ok, it contains at least one alphabet, one number and one special char")
else:
    #if the lenght of input is less than 8 then it will be consider as invalid
    print("Your password is invalid ,it must contains atleast 8 characters")
    
'''

output 1:

Create your password :jayakaviya
Your password is weak, it contains only alphabets or only numbers or only special chars

output 2:

Create your password :kaviya3$3
Your password is strong, it contains at least three alphabets, two numbers and one special char

output 3:

Create your password :happysunday4567#$%^
Your password is very strong ,it contains 16 count

'''




