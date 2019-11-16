

class A(object):
    def __init__(self,otherobj):
        self.otherobj=otherobj


#-------------another class -----------

class B(object):
    def __init__(self):
        self.aobj=A(self) #memory 
    def __del__(self):
        print('Destruct the object')

#--------------Function-------------------

def test():
    pass
   # bobj=B()
    
    
#------------functioncall-----------

#test()


