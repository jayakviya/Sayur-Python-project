sum = 0
a = int(input("Enter the number :"))
while a<=0 :
    print("Please enter the positive value")
    a = int(input("Enter the number :"))
for num in range(1,a+1) :
    sum = sum + num
print(sum)