#fibonacci term

def fibonacci(n):
  if n == 1 or n == 2 :
    return 1
  else :
    return fibonacci(n-1) + fibonacci(n-2)


#main area 
n = int(input("enter the number:"))
f = fibonacci(n)
print("the fibonacci term is:",f)
#for i in range(1,n+1):
# print(fibonacci(i),end=',')
