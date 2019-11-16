
def firstn(num):
    n=4
    while n <= num:
        yield n
        n=n+1
        
for x in firstn(15):
    print(x)