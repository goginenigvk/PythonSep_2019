class father:
    def __init__(self,param):
        self.o1=param

class child(father):
    def __init__(self,param):
        self.o2=param
     
    
obj=child(22)
father._father__init__
print(obj.o1, obj.o2)