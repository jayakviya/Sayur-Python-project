# From a given passage extract unique words and print them.
# Accept the passage as an input from the user

# 2. From a given passage find the longest and shortest word 
# and print the same. Accept the passage as an input from user

# 3. Accept 2 integers. print all nos which are mirror nos falling 
# between the range.
# eg: first no 300
#  second no 400
# 303,313,323.......393 

# try to incorporate error handling feature too in all the 
# above problems.
import re

passage = input("Enter your passage :")# to get input passage from user.
#To split the passage with spaceand . so use re function to split the passage.
newPassage = re.split(r'\s+|\.+', passage)

#to eliminate the empty string from user
newPassage =[word for word in newPassage if word]
#use max and min function to find the words of max len and min len

largeWord = max(newPassage,key=len)
shortWord = min(newPassage,key=len)
#finally print the longest and shortest word 
print(f"The largest word is '{largeWord}'")
print(f"The shortest word is '{shortWord}'")

'''
output 1:
Enter your passage :Python is a widely used general-purpose, high level programming language.It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation.It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code
The largest word is 'general-purpose,'
The shortest word is 'a'
'''