# anonymus function

n = lambda x,y : x+y

print(n(5,6))
str = lambda str1 : str1.upper()

print(str('lower'))


def hey(*args):
  sum = 0
  for arg in args:
    sum = sum + arg
  print(sum)
hey(5,6,6,7)