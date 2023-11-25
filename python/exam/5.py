s = input("enter a string")
l=d=0
for i in s:
  if i.isdigit():
    d += 1
  elif i.isalpha():
    l += 1
  else :
    pass
print("the letters:",l)
print("the digits:",d)
