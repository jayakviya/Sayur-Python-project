num = int(input("Enter your number"))
while num != 1:

    if num % 2 == 0 :
        num= int(num/2)
    else :
        num = 3*num+1
print("The resuut value ",num)

