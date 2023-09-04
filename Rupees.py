num = int(input("Enter the rupees :"))
if num >= 5 :
    num1 = int(num/5)
    remain = num % 5
    print(f"{num1}-5rupee coins")
    if remain > 0 :
        if remain >= 2 :
            num2 = int(remain/2)
            remain1 = remain % 2
            print(f"{num2}-2rupee coins")
            if remain1 == 1 :
                print("1-1rupee coin")
        else :
            print(f"{remain}-1rupee coin")
else :
    if num >= 2 :
        num3= int(num/2)      
        remain2 = num% 2
        print(f"{num3}-2rupee coins")
        if remain2 == 1 :
            print(f"{remain2}-1rupee coins")
    else :
        print(f"{num}-1rupee coin")



