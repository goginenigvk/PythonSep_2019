

class sample:
    def __init__(self):
       self.name='hello'
  

    def displayname(self,name):
        self.name=name
        print('name is ',name)
        print('name is self',self.name)

    def displayloc(self,location):
        print('location is',location, self.name)
    

s=sample()
s.displayname('Raja')
s.displayloc('Bangalore')
