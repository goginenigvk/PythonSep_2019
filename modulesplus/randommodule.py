

import random as r 

print(r.randint(10000,100000))

print(r.random())

print(r.randrange(5,10,3)) # 0

listseq=['one','two',3,4] #string, tuple ,list 
tupleex=(1,3,6,9,4,0)
print(r.choice(listseq)) # one item 

print(r.choices(listseq)) #one or more item in list 
print(r.choices(tupleex,k=3)) #one or more item in list 

# ABC12345


numbers=[8,9,2,6,8]
print(r.shuffle(numbers))
print(numbers)

