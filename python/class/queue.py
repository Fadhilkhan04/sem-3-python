class stack :

  def __init__(self):
    self.items = []
  
  def is_empty(self):
    return self.items == []
  
  def enqueue(self,value):
    return self.items.append(value)
  
  def dequeue(self):
    return self.items.pop(0)


s = stack()

while True:
  print("1.enqueue")
  print("2.dequeue")
  print("3.display")
  print("4.quit")

  ch = int(input("enter the choice u want:"))
  
  if ch == 1:
    val = int(input("enter the number :"))
    s.enqueue(val)
    continue
  elif ch == 2:
    if s.is_empty():
      print("queue is empty")
    else:
      print("dequeued item is:",s.dequeue())
    continue
  elif ch == 3:
    print(s.items)
  elif ch == 4:
    print("thankyou")
    break
  else:
    print("enter the right choice")
    continue