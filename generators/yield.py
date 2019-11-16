def mygen():
    x=5
    print('x value is ',x)
    
    yield 

    x=x+2
    print('x value is',x)
   
    yield

    x+=1
    print('x value after second yield',x)

    return x



for i in mygen():
    print(i)
    