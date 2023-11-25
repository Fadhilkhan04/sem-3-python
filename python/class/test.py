#python object oriented  programming
#learnt to create class
#difference btw class and instance of that class
#initialize class attributes and create method
class employee:
  
  def __init__(self,first,last,pay):
    self.first=first
    self.last=last
    self.pay=pay
    self.email=first + '.' +last+'@company.com'
    self.fullname=first + ' '+last
   
 # def fullname(self):
    #return '{} {}'.format(self.first,self.last)

emp_1=employee('fadhil','khan',70000)
emp_2=employee('ali','shazin',60000)

print(emp_1.email)
print(emp_2.pay)
print(emp_2.last)
print(emp_1.fullname)
#print(emp_1.fullname())
#print(employee.fullname(emp_1))