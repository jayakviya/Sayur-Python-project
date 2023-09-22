########### Program 5 #######
  # Write a program to run a cafe
  #  Cafe should have inventory, sales data and profit
import re 

total_costPrize=500
Cafe_Menu=["coffee","tea","greentea","blacktea"]
ordered_list=[]
Cafe_price=[20,15,30,45]
total=0
# print("Welcome to our shop!")
# print("Please let us know what do you want")
# print("Here our menu card :")
# for i,food in enumerate(Cafe_Menu):
#     print(f" {i+1} - {food}")
# print()
while True:
    item=input("what do you want?")
    order=""
    no_ofItem = re.findall("\d+|\d+",item)
    things = re.findall("(coffee|tea|blacktea|greentea)",item)
    print(no_ofItem)
    print(things)
    for i in range(len(Cafe_Menu)):
        if (item==Cafe_Menu[i]):
            b=True
            quantity = int(input(f"Enter number of {item} you need ? "))
            order=f"{quantity} {item} and its price is {quantity*Cafe_price[i]}"      
            total=total+(Cafe_price[i]*quantity)
            ordered_list.append(order)
        else:
            print(f"Sorry sir...{item} is not available")
            b= int(input("Enter 1 to cancel order or 0 to continue ordeer :"))
            if b==1:
                print("Thankyou for coming our shop")
                       
                break
print()
print(f"Your Ordered list : {ordered_list}")
print(f"Your total bill amount is : {total}")
if total<total_costPrize:
    print(f"You had loss because your total profit = {total} is < total invested amount per day = {total_costPrize}")
elif total>total_costPrize:
    print(f"You had get profit your total profit = {total} is > total invested amount per day = {total_costPrize}")