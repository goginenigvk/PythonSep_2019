
y=10 #global 

def inner():
    x=5 #local 
    global y
    y=y+1
    print('x is',x)
    print('y is',y)

inner()
print(y)
print(y)