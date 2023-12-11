class value:
  def __init__(self,a,b):
    self.a=a
    self.b=b
    
class operation(value):
  #def __init__(self,a,b):
   # value.__init__(self,a,b)
  def add(self):
    print("add is:",self.a+self.b)
c=operation(11,23)
c.add()