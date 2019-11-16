
class Parent1():
    def education(self):
       print('UG')

class Parent2(): 

   def property(self):
       print('in parent property')

   pass

class Child(Parent2,Parent1):
      pass

childobj=Child()

childobj.property()
childobj.education()
print(Child.mro())



