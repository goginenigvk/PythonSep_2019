

#map(function,iterable )
numbers=[1,2,4,5,6]
#1+5 2+5 4+5 
newlist=[]

for i in numbers:
    newlist.append(i+5)

print(newlist)

#lamda functions 
n=lambda i: newlist.append((i for i in numbers))
newl=n(numbers)
print(newlist)


x=lambda  a: a+2 #int
print(x(5))



