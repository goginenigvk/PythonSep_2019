setex={1,3,4,6,8,0,8,3}
print(setex)

# set cannot have mutable objects - list set dict
data={34.56,'summer',(2,4,6,6,4)}
print(data)
x={}

print(x)

listx=[2,4,6,2,4,6]
setlist=set(listx)
print(setlist)

setlist.add(8)
print(setlist)

setlist.discard(41)
print(setlist)

setlist.remove(2)
print(setlist)

listnum=[1,2,3,4]
setlist.update(listnum)
print(setlist)

set1={12,13,15}
set2={23,13,89}
# set3=set1+set2 

print(set1 | set2)
print(set1.union(set2))
print(set1 & set2)
print(set1.intersection(set2))
print(set1 - set2)
print(set1.difference(set2))

set1.pop()
print(set1)

print(set1^set2) #symeteric 
print(set1.symmetric_difference(set2))

s={1,5,6,3,7}
fz=frozenset(s)
print(type(fz))
print(fz)


set()

fz1=frozenset()
print(fz1)

