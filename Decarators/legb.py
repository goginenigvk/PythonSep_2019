
a=10 #G
def outer():
    a=15 #E 
    def inner():
        a=20 # L 
        print(a)
    inner()

outer()
print(a)