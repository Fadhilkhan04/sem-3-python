class calc:
  __hidevar = 0
  def sum1(self,a,b):
    self.__hidevar = a + b
    print(self.__hidevar)
  def sub(self,a,b):
    self.__hidevar = a - b
    print(self.__hidevar)
  def mult(self,a,b):
    self.__hidevar = a * b
    print(self.__hidevar)
  def div(self,a,b):
    self.__hidevar = a / b
    print(self.__hidevar)

obj = calc()

obj.sum1(4,2)
obj.sub(4,2)
obj.mult(4,2)
obj.div(4,2)
