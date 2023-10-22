def sum(list1):
    if len(list1) == 1:
        return list1[0]
    else :
        return ((list1[0]+sum(list1[1:])))
list1 = [12,45,23]
sumOfList = sum(list1)
print(sumOfList)