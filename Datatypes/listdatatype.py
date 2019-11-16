x=[]
print(x)

person1 =['John',45,600.45,'USA']
person2 =['RAM',22,600.45,'INDIA']
print(person1)

for i in person1:
    print(i)

print(type(person1))



#list() - LIFO

print(person2+person1)

print(person1*4)

# adding elemets into the list 
# Removing elemets  from the list 

person1.insert(1,'hello')
print(person1)

person1.append('Poland')
print(person1)


person1.pop()
print(person1)

person1.pop(3)
print(person1)

person3=person1
print(person3)

numbers=[1,4,9,0,3,10]
numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
numbers.sort()

countries= ['Poland','AUS','UK']
countries.sort(reverse=True)
print(countries)

print(len(person1))

print(person1.count('USA'))


countries.remove('UK')
print(countries)

countries2=['SG','USA']

countries.extend(countries2[1])
print(countries)

name="HEllo"
print(list(name))




yes=True
print(list(yes))

numb=[3,1,8,4,9]
co=['poland','USA']
both=numb+co
print(both)