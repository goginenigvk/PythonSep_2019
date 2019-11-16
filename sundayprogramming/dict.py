listx=[1,4,5,6]
listy=[5,7,8,9,10]
listz=[]
for i in range(len(listx)):   
    listz.append([listx[i],listy[i]])

print(listz)


dict1={'one':1,'two':2,'k':20}
print(len(dict1))
for i in dict1:   
    keyt=(dict1.keys() for i in range(len(dict1)))
    valuet=(dict1.values() for j in range(len(dict1)))
for i in range(len(dict1)):
    p=next(keyt)
    c=next(valuet)
print(tuple(p),tuple(c))


