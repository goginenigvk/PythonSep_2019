person=('john',28,200.56)
print(person)
print(type(person))

names='Sachin','Dravid','Ganguly'
print(type(names))
print('-1 output',names[-1])
print(names[2])
print(names[1]) #Dravid 


names2=('Yuvaraj','Dhoni',20,24,names,(50,29,30))
print(names2)
print(names2[4][1])
print(names2[0][2])

numbers=2,6,8,5,9,6,2,['a','b','c']
print(numbers[2:3])
print(numbers[:])

print(numbers.count(9))
print(numbers.index(9))
for i in numbers:
    print(i)

del numbers #please try 
li =[1,2,8,78,90,32]
del li
print(li)
