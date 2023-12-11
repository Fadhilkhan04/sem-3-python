class bank:

  def __init__(self):
    self.balance = 0 

  def withdraw(self,val):
    if self.balance >= val:
      self.balance = self.balance - val
      print("current balance:",self.balance)
    else:
      print("insufficient balance")
  def deposit(self,val):
    self.balance = self.balance + val
    print("current balance:",self.balance)
  
b = bank()
b.deposit(2000)
b.withdraw(1500)
b.withdraw(1000)