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

passage = input("Enter your passage")
newPassage = re.split(r'\s+|\.+', passage)
print(newPassage)

largeWord = max(newPassage,key=len)
shortWord = min(newPassage,key=len)
print("The largest word is",largeWord)
print("The shortest word is",shortWord)