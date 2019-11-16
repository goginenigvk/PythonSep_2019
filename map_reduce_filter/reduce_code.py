from functools import reduce


numbers =[1,4,6,7,7,8,9,0]

sumnum=reduce(lambda a,b:a+b ,numbers)
print(sumnum)