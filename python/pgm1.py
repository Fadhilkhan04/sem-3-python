
def fact(n):
    #fact = 1
    #for i in range (1,n+1):
     #   fact=fact*i
    if n == 1 or n==0:
        return 1
        
    return n*fact(n-1)

# main area
n = int(input("enter the number to find factorial of :"))
x = fact(n)
print("the factorial is :",x)
