
def div_decorator(function):  #enclosed functions 
    def inner(x,y):
        if y==0:
            return 'give proper input .. zero is not allowed'
        return function(x,y)
    return inner

@div_decorator
def div(a,b):
    return a/b


print(div(4,5))
print(div(4,0))





