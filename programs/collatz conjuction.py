
# '''Write a program for Collatz_conjecture.
# # Collatz_conjecture means -  start with the input number. 
# # For even number , divide by 2 (n/2)
# # For odd number - 3n + 1
# # apply the above for the result number until the answer is 1.'''

num =[]
count =[]
for i in range(2):
    value = int(input("Enter your input:"))
    num.append(value)
    for n in num :
        c=0
        while n!=1:
            if n %2 ==0:
                n=n//2

            else:
                n=3*n+1
            c+=1
        count.append(c)
min_count = min(count)
print(f"the number {num[count.index(min_count)]} have minimum iterations {min_count}")
            

