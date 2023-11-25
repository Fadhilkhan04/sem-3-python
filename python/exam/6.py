
def marks(n):
  l =[]
  print("enter the marks of semester ",n)
  print("\n")

  for i in range(1,6):
    print("enter the marks of subject ",i)
    num = int(input())
    while (num < 0 or num >100) :
      print("invalid")
      print("enter subject marks again",i)
      num = int(input())
    else :
      l.append(num)
  return l
    
# main area

l1 = marks(1)
print("\nmax marks in sem 1 is :",max(l1))
l2 = marks(2)
print("\nmax marks in sem 2 is :",max(l2))
l3 = marks(3)
print("\nmax marks is sem 3 is :",max(l3))