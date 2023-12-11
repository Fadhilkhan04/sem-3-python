class value:
  def first(self):
    self.a=int(input("Enter the a value"))
    
  def second(self):
    self.b=int(input("Enter the b value"))
    
class operation(value):
  def add(self):
    super().first()
    super().second()
    self.c=self.a+self.b
    print("The sum is:",self.c)
c=operation()
c.add()