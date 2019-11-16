import datetime as dt
class A: 

    ''' kskasd dk  dd '''
    __slots__=("anyvalue","Python")

    def __init__(self,anyvalue):
        self.anyvalue=anyvalue

    def __hash__(self): # int 
        return hash(self.anyvalue)

    def __index__(self):
        return 3

    def __dir__(self):
        return ['one','Two']


    def showvalues(self,name,age,sal) -> str:
        return name

a=A(8)
a1=A('Python')
print(hash(a))

print(hash(a1))
print(hash('Python'))

list1=[2,4,5,6,7,8]
print(list1[a1])

print(dir(a))

print(__name__) # __main__ module 
print(dt.__name__) # datetime 
print(a1.__class__)
print(a1.__class__.__name__)
#print(a1.__dict__)
print(a1.__slots__)
print(A.__doc__)



