def fibonacci (n) :
  if n == 1 or n == 2 :
    return 1
  else :
    return fibonacci (n-1) + fibonacci (n-2)

f = int(input ("enter the number to find the fibonacci of that term :"))
print (fibonacci(f))