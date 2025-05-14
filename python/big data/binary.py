data = [1,5,15,23,43,56,58,61,69,83,99]

a = int(input("enter the element you will like to search for :"))

found = -1
left = 0
right = len(data)

while left <=right:
  mid = (left+right)//2
  
  if data[mid] == a:
    found = mid
    break

  elif data[mid] < a:
    left = mid + 1
  else :
    right = mid - 1

if found == -1:
  print("not found")
else:
  print("found at :",found+1)