def fact(n):
  fact = 1
  while (n>0):
    fact = fact * n
    n -= 1
  return fact
val = fact(4)
print(val)