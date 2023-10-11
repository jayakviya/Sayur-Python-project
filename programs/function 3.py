"""
Problem 3:
  In the input, find the first A and last A, print all the letters between these two A. 
  If there is no A or 2nd A is not found, find the first B after the first A (if there is a A) and last B and print all the letters between these two B. 
  
  If there is no B or 2nd B is not found, find the first C after the first B (if there is a B) and last C and print all the letters between these two C. 

"""
def print_letters(alpha,inputString):
    inputString = inputString.upper()
    first_accurence = inputString.find(alpha)
    last_accurence = inputString.rfind(alpha)
    alpha_found=False
    
    if first_accurence!=-1:
        if first_accurence!= last_accurence:

            middle_letters = inputString[first_accurence+1:last_accurence]
            print(f"The letters between {alpha} is {middle_letters}")

            alpha_found=True
            return alpha_found
        
        else:
            print(f"There is only one {alpha}")
            inputString = inputString[first_accurence+1:]
            first_accurence = 0
    else :
        print(f"There is no {alpha} in your string")

    return alpha_found
    
        
#maincode
inputString =  input("Enter your string :")
alpha_found = {}
for i in range(26):
    alpha = chr(65+i)
    print_letters(alpha,inputString)
    if alpha in alpha_found and alpha_found[alpha]:
        break

   









        