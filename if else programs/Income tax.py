income = int(input("Enter your annual income :"))
tax = 0
if income <= 250000:
    tax = 0
    print("Income Tax =",tax)
elif income <= 500000:
    tax = (income-250000)*0.05
    print("Income Tax =",tax)
elif income <= 1000000:
    tax = 12500 + (income-500000)*0.2
    print("Income Tax =",tax)
else :
    tax = 112500 + (income-1000000)*0.3
    print("Income Tax =",tax)
