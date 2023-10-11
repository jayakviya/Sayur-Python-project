"""
Problem 1
In the input, find the first A and last A, print all the letters between these two A.

Problem 2:
  In the input, find the first A and last A, print all the letters between these two A. 
  If there is no A or 2nd A is not found, find the first B  and last B and print all the letters between these two B. 
  If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C. 

Problem 3:
  In the input, find the first A and last A, print all the letters between these two A. 
  If there is no A or 2nd A is not found, find the first B after the first A (if there is a A) and last B and print all the letters between these two B. 
  
  If there is no B or 2nd B is not found, find the first C after the first B (if there is a B) and last C and print all the letters between these two C. 

"""
def print_letters(alpha,inputString):
    inputString = inputString.upper()
    first_accurence = inputString.find(alpha)
    last_accurence = inputString.rfind(alpha)
    alpha_found = False
    if first_accurence!=-1:
        middle_letters = inputString[first_accurence+1:last_accurence]
        print("The letters between A is,",middle_letters)

        alpha_found=True
        if first_accurence == last_accurence:
            print("There is only one 'A'")
    else :
        print("There is no 'A' in your string")
        
#maincode
inputString =  input("Enter your string")
alpha = 'A'
print_letters(alpha,inputString)






        