########## Problem 3 ############
#Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 green bags (each Rs 1500)
#Customers can buy one or more bags at a time.
#The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
#Display total sales and total number of bags sold
import re
noOfbags = 0
sales = 0
bags = ["red","green"]
cost = ["1000","1500"]
stack = ["100","200"]
while (noOfbags < 10 and sales <10000):
    askcustomer = input("what colour of bags do you want red or green?") 
    noOfwantedBags = re.findall(r"\d+|\d+",askcustomer)
    wantedBags = re.findall(r"red|green",askcustomer)
    print(noOfwantedBags)
    for i ,bag in enumerate(wantedBags):
        if bag in bags:

            if bag == "red":
                noOfbags += int(noOfwantedBags[i])           
                sales += int(noOfwantedBags[i])*cost[0]
            elif bag == "green":
                noOfbags +=int(noOfwantedBags[i])
                sales +=  int(noOfwantedBags[i])*cost[1]
print("No of bags sold =",noOfbags)
print("Total sales amount:",sales)

        
   

        


