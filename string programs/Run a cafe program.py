########### Program 5 #######
  # Write a program to run a cafe
  #  Cafe should have inventory, sales data and profit
import re 

total_costPrize=500
Cafe_Menu=["coffee","tea","greentea","blacktea"]
ordered_list=[]
Cafe_price=[20,15,30,45]
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
    things = re.findall("(coffees?|teas?|blackteas?|greenteas?)",item)
    print(no_ofItem)
    print(things)
    b=True
    for i in range(len(Cafe_Menu)):
        if things in Cafe_Menu:
            b=True
            quantity = int(input(f"Enter number of {things} you need ? "))
            order=f"{no_ofItem} {things} and its price is {no_ofItem*Cafe_price[i]}"      
            total=total+(Cafe_price[i]*no_ofItem)
            ordered_list.append(order)
        b=False
        break
        if b:
            print(f"Sorry sir...{things} is not available")
        if int(input("Enter 1 to cancel order or 0 to continue ordeer :")):
        
            break
#                 print("Thankyou for coming our shop")
                       
#                 break
print()
print(f"Your Ordered list : {ordered_list}")
print(f"Your total bill amount is : {total}")
# if total<total_costPrize:
#     print(f"You had loss because your total profit = {total} is < total invested amount per day = {total_costPrize}")
# elif total>total_costPrize:
#     print(f"You had get profit your total profit = {total} is > total invested amount per day = {total_costPrize}")