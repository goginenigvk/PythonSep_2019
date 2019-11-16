from abc import ABC,abstractmethod
# super - Object, Exception - BaseException, Abstract class -ABC
#abstract base class 


class AbstractClass(ABC): 
    def __init__(self,side):
        self.side=side
     
    @abstractmethod
    def dosomecode(self):
        pass 

    def show(self):
        print('in show method')

class ConcreteClass(AbstractClass):
    
    def dosomecode(self):
        print('do some code')


class ConcreteClass2(AbstractClass):
    
    def dosomecode(self):
        print('do some code 2')


#ab=AbstractClass(15)

conobj= ConcreteClass(9)
conobj.dosomecode()




