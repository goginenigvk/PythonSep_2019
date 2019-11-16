
#decor 1 - upper cases 
def upper_greet(func):
    def inner():
        existordinarygreet=func()
        return existordinarygreet.upper()
    return inner

#decor2 - split
def split_greet(func):
    def wrpper():
       existordinarygreet=func()
       return existordinarygreet.split()
    return wrpper

@split_greet #first call 
@upper_greet # second call 
def ordinarygreet():
     return 'Good Morning'
    

print(ordinarygreet())

upperobj= upper_greet(ordinarygreet)
splitobj = split_greet(ordinarygreet)
print(upperobj())
print(splitobj())






    