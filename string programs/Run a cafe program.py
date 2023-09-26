########### Program 5 #######
  # Write a program to run a cafe
  #  Cafe should have inventory, sales data and profit
import re 

total_costPrize=500
Cafe_Menu=["coffee","tea","greentea","blacktea"]
#ordered_list=[]
Cafe_price=[20,15,30,45]

total = 0 # initialise the total 
while True:
    item=input("what do you want?")
    no_ofItem = re.findall("\d+|\d+",item)
    things = re.findall("(coffees?|teas?|blackteas?|greenteas?)",item)
    print(things)
    print(no_ofItem)
    for i in range(len(things)): # to execute the for loop for user's no of order
        if things[i] in Cafe_Menu:
            no_ofItem[i]=int(no_ofItem[i])
            for j in range(len(Cafe_Menu)): #to check if the item is matching

                if things[i] == Cafe_Menu[j]: # to find out the place of the thing[i] in cafemenu
                    print(f"{no_ofItem[i]} {things[i]} is Rs.{no_ofItem[i]*Cafe_price[0]}")
             
                    total+=no_ofItem[i]*Cafe_price[0]
        else:
            break
        
            
    b=int(input("Enter 1 to cancel order or 0 to continue ordeer :"))
    if b==1:
        break
    else:
        continue
        
print(f"Total sale bill amount is : {total}")
if total<total_costPrize:
    print("you had get loss")
elif total>total_costPrize:
    print("You had get profit")
    '''
output 1:
what do you want?4 tea 3 blacktea
['tea', 'blacktea']
4 tea is Rs.60
3 blacktea is Rs.135
Enter 1 to cancel order or 0 to continue ordeer :1
Your total bill amount is : 195
you had get loss

output 2:
what do you want?3 coffee and 4 blacktea 5 greentea
['coffee', 'blacktea', 'greentea']
3 coffee is Rs.60
4 blacktea is Rs.180
5 greentea is Rs.150
Enter 1 to cancel order or 0 to continue ordeer :0
what do you want?5tea 6 blacktea
['tea', 'blacktea'] 
5 tea is Rs.75      
6 blacktea is Rs.270
Enter 1 to cancel order or 0 to continue ordeer :1
Total sale bill amount is : 735
You had get profit

'''