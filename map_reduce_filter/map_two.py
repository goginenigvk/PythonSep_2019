

from functools import reduce
def squaren(n):
    return n*n

list1=[1,7,0]
list2=[9,4,5,9]

output=map(squaren,list1)
print(list(output))


outputl=map(lambda n: n**3, list1)
outputreduce=reduce(lambda a,b:a+b,outputl)
print(outputreduce)

ouputltwolist=map(lambda n,m: [(n*n),(m*m)],list1,list2)
print(list(ouputltwolist))



