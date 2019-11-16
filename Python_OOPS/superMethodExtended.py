
#Super() - Inheritannce 
class MyParentClass(object):

    def __init__(self):
        pass


    def show(self):
        pass


class Subclass(MyParentClass):
    def __init__(self):
        MyParentClass.__init__(self)



#.....Bleow code python3
class Subclass2(MyParentClass):
    def __init__(self,x,y):
        pass
      #super()__init__(x,y)
        