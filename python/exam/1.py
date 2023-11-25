#factorial

def fact(n):
  fact = 1
  while(n>0):
    fact = fact*n
    n = n - 1
  return fact

#main area 

n = int(input("enter a number:"))
f = fact(n)
print("factorial is:",f)