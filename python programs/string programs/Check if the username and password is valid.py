''' Check if the username and password is correct. 
     Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
     passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
     name of the company mentioned in the username, followed by any 3 numbers.
     eg username : myname@sayur.com. password - mnamesay123 
     '''

import re

userName = input("Enter your username:")#to get username 
user_passWord = input("Enter your password")#to get user password


check = re.search(r'@.*\.com', userName)#check if the username contain the spec char'@' and it ends with .com or .edu and ext.
if check:
    print("Username is valid")
else:
    print("Username is invalid ")
part1 =  userName.split("@")[0]
part2 =  userName.split("@")[1].split(".")[0]

#construct password
newPassword = part1[0]+part1[2] + part1[-3:]+part2[:3]
          


if user_passWord.startswith(newPassword) and re.search(r'\d{3}',user_passWord):
    print("Your password is correct")
else:
    print("Your password is incorrect")
