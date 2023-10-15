########### Program 5 #######
  # Write a program to run a cafe
  #  Cafe should have inventory, sales data and profit
import re 
#define menu card as dictionary it contains the available quantity and the price of the corresponding item

menu = {"coffee":{'quantity':50,'price':20},"tea":{'quantity':30,'price':30},
        "greentea":{'quantity':30,'price':50},"blacktea":{'quantity':45,'price':70}}
total_cost = 4500 #initialize the cost value

total = 0 # initialise the total                  
order = 0 


while order <= 10:#I have given the limited value to the while loop

    item=input("what do you want?")
#bring the input from the user

    items = re.findall(r'(\d+)\s*(\w+)',item)#seperate the quantity and item as tuples.

    for quantity ,item_name in items:#for loop will iterate the no of given items
        
        quantity = int(quantity)#type casting the string quantity value into integer

        if item_name in menu:#check if the given item is in our cafe

            item_details = menu[item_name]# to collect the details of item
            
            item_price = menu[item_name]['price']#to store the price of item
           
#check if the quantity of item that user want is available in our cafe
            if item_details['quantity'] >=quantity:

                print(f' {quantity} {item_name} is {item_price*quantity} ')

                total += quantity * item_price     #calculate and store the value of total 
                item_details['quantity'] -= quantity  #to reduce the quantity of item in the menu because it sold
                order += 1  
               
#if the required quantity is not available in our cafe then this part execute
            else:
                print(f'Sorry {item_name} is not in stock in sufficient quantity')
#if the item is not in the menu then the following will execute
        else:
            print(f'Your order {item_name} is not in the menu card')
#ask the user if he/she want to buy else 
    choice = int(input('Do you want to continue your order press 1 or press 0 to exit'))#to store the user's choice
    if choice == 0:#choice is 0 then loop breaks otherwise it continues
        break
    else:
        continue
    
print(f"Your total bill amount is {total}")#to print the total amount 
if total >= total_cost:#to check if we get lose or profit
    print("You get profit")
else:
    print("you get loss")
    
