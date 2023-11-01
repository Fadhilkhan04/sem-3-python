def marks(num):
  l = []
  print("\nenter the marks of semester ",num)
  print("\n")

  for i in range(1,6):
    print("enter the marks of subject",i)
    n1 = float(input())

    while(n1<0 or n1>100):
      print("Invalid Marks try again")
      print("enter the marks of subject ",i)
      n1 = float(input())
    else:
      l.append(n1)

  return l

#main area
l1=marks(1)
print("\nthe maximum marks in semester 1 is :",max(l1))
l2=marks(2)
print("\nthe maximum marks in semester 2 is :",max(l2))
l3=marks(3)
print("\nthe maximum marks in semester 3 is :",max(l3))


    
