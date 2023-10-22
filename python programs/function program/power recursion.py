def power(x,n):
    if n==0:
        return 1
    else:
        return(x*power(x,n-1))
    
pow = power(3,5)
print(pow)
