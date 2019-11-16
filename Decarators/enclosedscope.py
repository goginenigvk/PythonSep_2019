y=10 #global variable 

def outer(): #enclosed function 
    z=4  #enclosed variable 
    global y
    y=y+1
    def inner(): #nested function 
        x=4  #local variable 
        global y
        y=y+2
        nonlocal z
        z=z+1
        print('x is',x)
        print('y is',y)
        print('z is',z)
    inner()
    print('z is',z)
    #print('x is',x)

outer()