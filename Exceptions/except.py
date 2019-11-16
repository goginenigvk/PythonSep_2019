

try:
    a = int(input('enter first value '))
    b = int(input('enter second value '))

    sumtwo=a+b
    print('The Result', sumtwo)

    dvisonzero=a/b
    print("the Result division",dvisonzero)
    

except (ZeroDivisionError,ValueError):
    print('Enter only integer values and Dont provide input zero')

print("finally code")

 