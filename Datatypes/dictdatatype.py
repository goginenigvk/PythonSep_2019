x={}
print(type(x))
print(x)

names={'India':'Sachin','SA':'AB','AUS':'Ponting','india':'Rahul'}
print(names['SA'])
#print(names['RUS'])

score={1:3,2:4,3:6}
print(score[1])


listdict={ 'name':'John','age':17,'address' :['Delhi','Bangalore']}
print(listdict['address'])

for i in listdict:
    print(listdict[i])

print(listdict.keys())
print(listdict.values())
print(listdict.items())

listdict['name']='Deep'
print(listdict)


listex=[(1,'A'),(2,'B'),(3,'C')]

convlist=dict(listex)
print(convlist)

del listdict['name']
print(listdict)

listdict.pop('age')
print(listdict)

listdict.popitem()
print(listdict)

print(convlist)
get2=convlist.get(2)
print(get2)

score1={1:3,2:4,3:6,4:1}
for i in score1.items():
    print(i)

