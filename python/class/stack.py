class stack :

  def __init__(self):
    self.items = []
  
  def is_empty(self):
    return self.items == []
  
  def push(self,value):
    return self.items.append(value)
  
  def pop(self):
    return self.items.pop()


s = stack()

while True:
  print("1.push")
  print("2.pop")
  print("3.display")
  print("4.quit")

  ch = int(input("enter the choice u want:"))
  
  if ch == 1:
    val = int(input("enter the number :"))
    s.push(val)
    continue
  elif ch == 2:
    if s.is_empty():
      print("stack is empty")
    else:
      print("popped item is:",s.pop())
    continue
  elif ch == 3:
    print(s.items)
  elif ch == 4:
    print("thankyou")
    break
  else:
    print("enter the right choice")
    continue