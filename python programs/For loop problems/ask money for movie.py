
############## Problem 2 ################
#Use For loop, break and continue as needed.
# You need Rs 1000 to go to movie. you are asking your parents for money. your parents give you a
# some money. Ask your parents for money until you get Rs1000 or a maximum of 5 times.
# Each time they give you some money, you need to print how much money you got so far and print "Thank you.".
# Print "Thank you " only if the money is > Rs 10. If money is less than or = Rs 10, don't add it
# towards the Rs1000 that you need. Use Continue stmt as needed.
# Print how many times you had to ask your parents to get this money.


money = 0
askMoney = int(input("I want to go for a movie please give me money:")) # ask the money and store it to a variabke
for i in range(4):
    if askMoney < 1000:# i want 1000 if askmoney is less than 1000 then I should ask money continuingly
        if askMoney > 10:#we can add money only it is more than 10 rs.
            money += askMoney
            if money <  1000:
            #in the loop adding given money and the added money is still less than 1000 we should ask again
                print("Thank you!")#Say thankyou only your parents give you more than 10 rs.
                askMoney = int(input("Gimme some more money :"))# ask again for money
                if (i+2)==5 :# if you ask 5 times than its a limiting time so you should not ask again
                    print("you asked money for 5 times and it is the limited time")
                else:      #otherwise you should  continue       
                    continue
            else :#if given money is >=1000 than you stop for asking money
                print("Thank you I have enough money")
                print(f"{i+1} times I ask for money")#print how many times you asked
                break
          
        else:# if your parents gave less than 10 rs you can't add it to the money and don"t say thank you
            money=money
            askMoney = int(input("Gimme some more money :"))
            if (i+2)==5 :# if you ask 5 times than its a limiting time so you should not ask again
                    print("you asked money for 5 times and it is the limited time")
            else:      #otherwise you should  continue       
                continue
            
'''
output 1:
r loop problems/ask money for movie.py"
I want to go for a movie please give me money:300
Thank you!
Gimme some more money :500
Thank you!
Gimme some more money :60
Thank you!
Gimme some more money :230
Thank you I have enough money
4 times I ask for money

output 2:
I want to go for a movie please give me money:100
Thank you!
Gimme some more money :200
Thank you!
Gimme some more money :300
Thank you!
Gimme some more money :100
Thank you!
Gimme some more money :50
you asked money for 5 times and it is the limited time
output 3:
I want to go for a movie please give me money:10
Gimme some more money :10
Gimme some more money :20
Thank you!
Gimme some more money :10
Gimme some more money :10
you asked money for 5 times and it is the limited time
''' 
    
        

