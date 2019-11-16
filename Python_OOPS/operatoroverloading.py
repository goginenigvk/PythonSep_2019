
class OperatorOverloading:

    def __init__(self,count):
        self.count=count 

    def __add__(self,*other):
        return self.count+other.count
    
    def __sub__(self,other):
        return self.count-other.count

    


operator1=OperatorOverloading(15)
operator2=OperatorOverloading(30)
operator3=OperatorOverloading(45)
print(operator1+operator2)
print(operator1-operator2)
print(operator1+operator2+operator3)
print(operator1+operator3)

