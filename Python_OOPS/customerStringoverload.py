
class Customer:
    def __init__(self,cname):
        self.customername=cname

  

    def __str__(self):
        return self.customername


    def __add__(self,other):
           totalcustomernames =self.customername+other.customername
           cfinaltoal=Customer(totalcustomernames)
           return cfinaltoal


c1=Customer('John')
c2=Customer('Doe')
c3=Customer('Mr.')
c4=Customer('python')
print(c1+c2+c3+c4)






