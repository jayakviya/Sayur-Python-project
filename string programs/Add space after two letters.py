inputString = list(input("Enter your input string: ")) # get the input string
outputString = "" 

for index,char in enumerate(inputString): # for loop will execute until index = len(inputstring)-1
    if index >=2 : # consider the 3rdplace letter 

        if index % 2 == 0: # this indicates that give space after every pair of letters

            outputString +=  inputString[index-2] +inputString[index-1]+ " "
if len(inputString) % 2 != 0: # if the length of the input is odd it should be placed the last single character in the output
                            #so we use this code to print the last letter

    outputString += inputString[-1] #inputString[-1] defines the last term of the list

if len(inputString) >= 2 and len(inputString) % 2 == 0: # if the lenght is even then it should be placed the last two letters of the input 
    outputString += inputString[-2] + inputString[-1]


           
print("Output:", outputString)

'''
output
------
Enter your input string: asdfghjk
Output: as df gh jk'''


