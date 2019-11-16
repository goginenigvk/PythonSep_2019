

def outer():
    x=3
    def inner():
        y=4
        result=x+y
        return result 
    return inner() # function can itself 
    

a=outer() #function to function

print(a)

