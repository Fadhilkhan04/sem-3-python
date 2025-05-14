class person:
  def __init__(self,fname,lname):
    self.fname = fname
    self.lname = lname

  def print(self):
    print(f'{self.fname} {self.lname}')

class student(person):
  pass

a = student('fadhil','khan')
a.print()
