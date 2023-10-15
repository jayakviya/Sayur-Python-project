'''Write a Python program to sort a list of tuples using Lambda.
[("apple", 50),("orange", 15) ,("mango", 30)]
lambda functios - sort by name, sort by cost'''


items = [("apple", 50),("orange", 15) ,("mango", 30)]

sortedByName = sorted(items,key = lambda x:x[0])
print("Sorted Names:")
for item in sortedByName:
    print(item)

sortedByCost = sorted(items,key=lambda x:x[1])
print("sorted costs:")
for item in sortedByCost:
    print(item)