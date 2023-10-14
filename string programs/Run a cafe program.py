########### Program 5 #######
  # Write a program to run a cafe
  #  Cafe should have inventory, sales data and profit
import re 
menu = {"coffee":{'quantity':50,'price':20,'profit':10},"tea":{'quantity':30,'price':30,'profit':5},
        "greentea":{'quantity':30,'price':50,'profit':10},"blacktea":{'quantity':45,'price':70,'profit':30}}
total_cost = 4250 

total = 0 # initialise the total                  #2300 - total profit value
order = 0 


while order < 2:

    item=input("what do you want?")


    items = re.findall(r'(\d+)\s*(\w+)',item)

    for quantity ,item_name in items:
        
        quantity = int(quantity)

        if item_name in menu:

            item_details = menu[item_name]
            
            item_price = menu[item_name]['price']
           

            if item_details['quantity'] >=quantity:
                print(f' {quantity} {item_name} is {item_price*quantity} ')

                total += quantity * item_price
                item_details['quantity'] -= quantity
                order -= 1
               

            else:
                (f'Sorry {item_name} is not in stock in sufficient quantity')
        else:
            print(f'Your order {item_name} is not in the menu card')
    choice = input('Do you want to continue your order press 1 or press 0 to exit')
    if choice == 0:
        break
    else:
        continue

print(f"Your total bill amount is {total}")
for items,details in menu.items():
     profit = item[details]['profit']*item[details]['quantity'] - menu[item_name]['quantity']
     
     print(f'Profit fot {item_name} is {profit}')

            
    
