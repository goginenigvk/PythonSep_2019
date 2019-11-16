""" 
#abs() - int/float
x=abs(20.30)
y=abs(-34.76)
print(x,y)


#all() - boolean - o, False, none 
listx=[2,3,9,2,4]
print(all(listx))

listx1=['raja',34,False]
for i in listx1:
    print(i)

#bin() -0b 
x=20
print(bin(20))

#bool() - True/False
listx2=[0]
print(listx2)
x=0
print(bool(listx2),bool(x))

#bytes() -
name='India is strong nation in ASIA'
namebyte=bytes(name,'utf-8')
print(namebyte)
print(type(namebyte)) """

#compile()
codes='x=2'
f=open('Functions/functionparam2.py','r')
strcode=f.read()
ccodes=compile(strcode,'functionparam2.py','exec')
print(ccodes)
exec(ccodes)

#exec()


#sum()
listsum=sum([1,6,9,5])
tuplesum=sum((1,7,0,3))
print(listsum,tuplesum)

#any() - true/false
any
all



