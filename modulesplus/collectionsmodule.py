
from collections import defaultdict
from collections import OrderedDict
from collections import Counter
from collections import ChainMap
from collections import namedtuple
from collections import deque




# map,reduce and filter 


#decorators - OOPS 
# Magic functions / Magic methods 
list1=[1,7,9,0]
tuple1=(1,7,9,0)
#print(dict(list1))
#print(dict(tuple1))
 
countryregion=[

('ASIA','INDIA'),
('AFRICA','SA'),
('X','YYY'),
('NORTHAMERICA','CANADA'),
('EUROPE','POLAND'),
('ASIA','JAPAN')
]
print(dict(countryregion))

#dict2={'1':'one','1':'TWO'}

listdefaultdict=defaultdict(list)
for region,country in countryregion:
    listdefaultdict[region].append(country)

print(list(listdefaultdict.items()))

intdefaultdict=defaultdict(list)
intdefaultdict['one']=1
intdefaultdict['two']=2
intdefaultdict['three']=3
intdefaultdict['two']=4
print(intdefaultdict)

orderdict=OrderedDict(countryregion) # list as an argument 
print(orderdict.items()) # insertion order 

listex=[1,3,6,7]
count=Counter( (country) for region,country in countryregion)
print(count)


dictone={'1':'one', '2':'two'}
dicttwo={'3':'three', '4':'four'}
dictthree={'5':'five'}

chainmapdict=ChainMap(dictone,dicttwo,dictthree)
print(chainmapdict['3'])

listone=[1,4,5,6,6,8]
listtwo=[8,9,14,16,1]
chainmaplist=ChainMap(listone,listtwo)
print(chainmaplist)
print(chainmaplist[5])
# please try this tomorrow  - assigment 


person=('Raja',20,'M')
#person[1]=34
person=('Mahesh',24,'M')
print(person)


person = namedtuple( 'person', 'name age gender')
# person datbase table - name age gender location qualification 

person1 =person(name='raja',age=24, gender='M')
print(person1)
print(person1.age)


lisnumbers=[4,5,6,2,5,3,5]
lisstrings=['one','two']
listdeque=deque(lisnumbers)
print(listdeque)
listdeque.appendleft('3')
listdeque.appendleft('200')
listdeque.append('1000')
print(listdeque)
listdeque.extendleft(lisstrings)
print(tuple(listdeque))


dq= deque(countryregion)
print(dq)
dq.appendleft('raja')
print(dq)
string='hello'
dq.extendleft(string)
print(dq)

dq.popleft() # first item at left - deleted 
dq.pop()
print(dq)











