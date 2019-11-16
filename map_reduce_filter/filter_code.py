

list1 = [1,2,3,4,5,6,7,8,9]

#filter(function,iterable)
evenfilter=filter(lambda x: x>5, list1)
print(list(evenfilter))



print(list(filter(lambda x: x%2 != 0, list1)))

