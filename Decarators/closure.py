
def outer():
    x=5
    def inner():
      print('hello')
      x=2
    return inner()

var=outer()
#referncevariable = functioncall()
print(var) #15

def function1():
    print('this is a function1')

def function2(func):
    print('this is a function2')
    function1()

function2(function1)
