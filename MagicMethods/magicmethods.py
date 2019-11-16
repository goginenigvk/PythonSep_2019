


# __add__, __sub__, __mul__....... +, -, * 

# __str__  == print()

class MagicMethod(object):
    def __init__(self,anyvalue):
        self.anyvalue=anyvalue

    def __abs__(self):
        return abs(self.anyvalue)

    def __round__(self):
         return round(self.anyvalue)
    
    def __add__(self,other):
        return self.anyvalue + other

    def __radd__(self,other):
        return self.anyvalue + other

    def __iadd__(self,other):
         self.anyvalue += other
         return self

    def __bool__(self):
           return self.anyvalue
  
    def __str__(self):
        return str(self.anyvalue)

    def __repr__(self):
        return self.anyvalue

    def __len__(self):
        return len(self.anyvalue)
    

obj=MagicMethod(-8)
obj2=MagicMethod(True)
obj1=MagicMethod('Python')
print(abs(obj))
print(round(obj))
print(obj+5) #add
print(5+obj) # radd
#obj+=8  # iadd 
obj+=19
print(obj.anyvalue)
print(bool(obj2))
print(type(str(obj)))
print(repr(obj1))
print(len(obj1))






