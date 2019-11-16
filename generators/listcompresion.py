
listcom=[ i for i in range(1000)]
print(listcom)
print(type(listcom))


tuplecom=(i for i in range(10))  # yield 
#print(tuplecom)
print(type(tuplecom))
while True:
   print(next(tuplecom))
   break
