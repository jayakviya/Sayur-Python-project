sum = 0
for x in range(1,7):
    mark=int(input(f"Enter your mark in subject {x} :"))
    sum += mark
print("Total = ",sum)
avg = (sum/6)
print("Average =",avg)
if avg < 50 :
    print("You failed")
elif avg <= 60 :
    print("You passed in Third class")
elif avg <= 70 :
    print("You passed in Second class")
else :
    print("You passed in First class")


