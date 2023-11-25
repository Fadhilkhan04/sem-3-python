#affix zeroes

def zeroes ( a,b,c):
  for i in range(a,b+1):
    num_str=str(i)
    num_len=len(num_str)
    zero = c - num_len
    print('0'*zero+num_str,end = ',')

#main area

a = int(input("enter the start value:"))
b = int(input("enter the end value:"))
c = int(input("enter the desired lenthg :"))

zeroes(a,b,c)