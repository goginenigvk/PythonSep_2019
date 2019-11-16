

def mygen():
    yield 'A'
    yield 'B'
    yield 'C'

gen=mygen()
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

listx=['A','B','C']
for i in listx:
    print(i)
  