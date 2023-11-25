#prime nos within a range
def prime(a,b):
  for num in range (a,b+1):
    for i in range(2,num):
      if (num % i == 0):
        print(f"{num} is not prime number")
        break
    else :
      print(f"{num} is prime number")

#main area
a = int(input("enter the start:"))
b = int(input("enter the end:"))


prime(a,b)