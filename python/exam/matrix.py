#addition of matrix

r = int(input("enter the rows"))
c = int(input("enter the columns"))
m1 = [[0]*r]*c
m2 = [[0]*r]*c

print("enter matrix 1")
for i in range(0,r):
  for j in range(0,c):
    print("enter element",i,j)
    m1[i][j] = int(input())

print("enter matrix 2")
for i in range(0,r):
  for j in range(0,c):
    print("enter element",i,j)
    m2[i][j] = int(input())

sum = [[0]*r]*c

for i in range(0,r):
  for j in range(0,c):
    sum[i][j] = m1[i][j] + m2[i][j]


    