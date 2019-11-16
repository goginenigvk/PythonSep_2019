
import os
super()
# abstraction and encapsulation 



class A:
    x=2  
    def __init__(self,name,age):
        self.name='hello' #protected 
        self.__age=age # private 

    def __show(self):
        print('in show method')

class B:
    pass

print(issubclass(B,A))
isinstance(B,A)


# isstance - Object ref, Class Name



#OOP - __init__ 
# ... self 
# ...Object    



