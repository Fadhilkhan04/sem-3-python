l = []
n = int(input("enter the number of elements:"))

for i in range (0,n):
    num = int(input("enter the element :"))
    l.append(num)

print("the list is:",l)
print("the max number in list is:",max(l))
print("the min number in list is:",min(l))