#To print the table for the number that is given by user
'''
for example if given number is 2 then
the output is
1 * 2 = 2 
2 * 2 = 4   
3 * 2 = 6   
4 * 2 = 8   
5 * 2 = 10  
6 * 2 = 12  
7 * 2 = 14  
8 * 2 = 16  
9 * 2 = 18  
10 * 2 = 20 
    
    '''
j = int(input("Enter the number: ")) # getthe input number from user
while j <= 0 :
    # We should sure that the user must give positive number
    print("Please enter the positive value")
    # if the user put negative or zero then this loop will never stop getting input from user until
    # they give a valid input
    # when user give valid input then the process will start
    j = int(input("Enter the number: "))
for num in range(1,11): # the range is 1-10
    num3 = num*j # we calculate the multiples of the given value with 1-10

    print(f"{num} * {j} = {num3} ")# finally print the table 