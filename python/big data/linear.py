data = [10,20,30,40,50]

a = int(input("enter the value u need to search for:"))
found = -1

for i in range(len(data)):
  if data[i] == a:
    found = i
    break

if found == -1:
  print("sorry your element was not found")
else :
  print("Your element was found at position :",found+1)