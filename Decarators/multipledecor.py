

# one function - one decor 
# one function - two decor (one more )
# two functions - same decor ? 

def div_decarator(func):
    def inner(*args):
        list1=[]
        list1=args[1:]
        for i in list1:
            if i==0:
                return 'provide proper input'
        return func(*args)
    return inner

@div_decarator
def div1(a,b):
    return a/b

@div_decarator
def div2(a,b,c):
    return a/b/c

print(div1(10,0)) #0 -- zero divison 
print(div2(0,5,6)) #0 --zero divison