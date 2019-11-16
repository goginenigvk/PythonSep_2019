

class Shape(object):
    def __init__(self,shapename,shapesize):
        self.shapesize=shapesize #9
        self.area=1000
        print('Shape name',shapename, self.shapesize)
    
    def displayshape(self):
        print(self.shapesize,self.area)
        print('no shape')


class Rectangle(Shape):
    def __init__(self):
        super().__init__('Rectangle',9)
        self.shapesize=self.shapesize+10
        self.area=self.area+2000
        print('shape of object is Rectangle',self.shapesize)

    def displayshape(self):
        super().displayshape()
        print('display shape is Rectangle')


class Square(Rectangle):
    def __init__(self):
        super().__init__()
        print('in sqaure class constructor',self.shapesize,self.area) 
       


r=Rectangle()
s=Square()





