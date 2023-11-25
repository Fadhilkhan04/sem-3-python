#fibonacci series

n = int(input("enter the number:"))
n1,n2 = 0 ,1
temp = n2
count = 0

if (n <= 0):
  print(" please enter a positive number")

elif (n == 1 ):
  print(" the factorial is : ",n1)

else :
  while (count < n):
    print (n1,end= " ")
    count += 1
    n1,n2 = n2 ,temp
    temp = n1+n2
  