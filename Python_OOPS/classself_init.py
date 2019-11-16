

class Customer:
  # self - implicit variable - pointing to current object 
  # first arugment in constuctor / instance method 
  # self - delare instance variable 
  # a,A,0-9,_

    def __init__(self,name):
        self.name=name
        print('constructor is being called')
        print(self.name)
        print('id of self',id(self))
# To declare instance variables and its intilization 
# atleast one agrument 
# constuction, ... default constuctor 
# constructor overalding is not available 

    def customerinfo(self):
        print(self.name)
        print('id  of self in metod',id(self))


c=Customer('hello')
c1=Customer('good mornings')


print(id(c))
c.customerinfo()




