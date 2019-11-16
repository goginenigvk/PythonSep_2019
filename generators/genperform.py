import random
import time

regions =['ASIA','AFRICA','EUROPE','NORTHAMERICA']
countries= ['India','SouthAfrica','Norway','Canada']

def people_list(num):
    results=[]
    for i in range(num):
        person={
            'id':i,
            'region':random.choice(regions),
            'country':random.choice(countries)
        }
    results.append(person)
    return results


def people_generator(num):
    x=2
    for i in range(num):
        person={
            'id':i,
            'region':random.choice(regions),
            'country':random.choice(countries)
        }
        yield person
    return x

        

t1=time.clock()
people=people_list(100)
t2=time.clock()

print('time taken for list',t2-t1)

1 
t1=time.clock()
people=people_generator(100)
t2=time.clock()

print('time taken for generator',t2-t1)