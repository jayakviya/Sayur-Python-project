inputString = input("Enter your input string: ") # get the input string
outputString = "" 

for index in range(len(inputString)): # for loop will execute until index = len(inputstring)-1

    if (index==len(inputString)-1):  #qwerty

        outputString += inputString[index]
    else:
        outputString = outputString+ inputString[index] + inputString[index+1] +" "
        outputString+=" "
    index+=2
           
print("Output:", outputString)





