'''
To find the electricity payment
for the electricity we use
'''
unit = int(input("Enter the unit consumed = "))
if unit > 500:
    if unit <= 100:
       amount = 0
       print("Amount=",amount)
    elif unit <= 400:
       amount (unit-100)*4.5
       print("Amount=",amount)
    elif unit <= 500:
       amount =1350 + (unit-400)*6
       print("Amount=",amount)
    elif unit <= 600:
       amount = 1950 + (unit-500)*8
       print("Amount=",amount)
    elif unit <= 800:
       amount = 2750 + (unit-600)*9
       print("Amount=",amount)
    elif unit <= 1000:
       amount = 4550 + (unit-800)*10
       print("Amount=",amount)
    elif unit > 1000:
       amount = 6550 + (unit-1000)*11
       print("Amount=",amount)
elif unit<=100:
    amount = 0
    print("Amount=",amount)
elif unit <=200:
    amount =(unit-100)*2.25
    print("Amount=",amount)
elif unit <= 400:
    amount = 225 + (unit-200)*4.5
    print("Amount=",amount)
else :
    amount = 1125 + (unit-400)*6
    print("Amount=",amount)