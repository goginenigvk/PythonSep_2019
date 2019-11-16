class myclass:
    x=1
    y=2

varref1=myclass()
varref2=varref1

varref1.x=11
varref1.y=12

print(varref1.x,varref1.y)
varref1.x=14
varref1.y=16

print(varref1.x,varref1.y)

 