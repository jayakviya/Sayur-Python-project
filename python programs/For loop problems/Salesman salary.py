
############## Problem  3  #################### 
#Calculate the monthly salary for the phone salesman
#Base monthly pay Rs10000. 
#For every 5 phones sold, Rs 5000 bonus.
#For every phone aftr the first 5 phones, Rs1100 per phone bonus.
#If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
# this month also, then he gets additional Rs5000.

monthlySalesList = [5,23,21,14,23,12,4,12,22,22,34,12]  # Sample number of phones sold in each month in a year
#FillinMissingCode - initialise all the variables needed
baseSalary= 10000
previousMonthSalary = 0
cumulativeBonus = 0
for month, phoneCount in enumerate(monthlySalesList):
    print (f"{month+1} month's salary before additional bonus {baseSalary}")
    if phoneCount>=5:
        currentMonthSalary= baseSalary+5000+(phoneCount-5)*1100
    else:
        currentMonthSalary=baseSalary
 
    if (previousMonthSalary >= 20000) and (phoneCount >=20) :
        currentMonthSalary+=5000
    else:
        currentMonthSalary=currentMonthSalary
    cumulativeBonus += currentMonthSalary-10000
    print("Bonus Amount =",cumulativeBonus)
    
    if cumulativeBonus >= 100000:
        currentMonthSalary+=currentMonthSalary*0.05
    print (f"{month+1} month's salary after additional bonus {currentMonthSalary}")
    previousMonthSalary = currentMonthSalary
    print("_____________________")       




    #check for condition #If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
    # this month also, then he gets additional Rs5000.

   
   
   