
def wish_upper(func):
    def inner():
        wishstring=func()
        print(wishstring)
        return wishstring.upper() #string object
    return inner #function can be 


@wish_upper
def wish(name):
    #print('hello! Good Morning')
    return 'hello! Good Morning'

#wish()
print(wish('USA'))

#dec=wish_upper(wish) #objectreference= decaratorfunction(function)
#dec()


