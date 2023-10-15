#buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user.

#find how many choc and cake the user can buy

noOfCake = 0
noOfChoc = 0
budget = int(input("Enter your budget:"))


while (budget >= 150) :  # if the user have more than 150 then this code is work
    if (budget > 200) :
        #buy choc
        noOfChoc += 1
        budget -= 200
    if (budget > 150):
        noOfCake += 1
        budget -= 150
print("No of choc you can bought:",noOfChoc)
print("No of cake you can bought",noOfCake)
    
   


