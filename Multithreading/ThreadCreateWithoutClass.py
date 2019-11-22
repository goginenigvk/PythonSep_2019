
from threading import Thread

# task which perfomed Thread 
def  displaySeq(name):
    for i in range(100):
        print('Thread value is ',i,name)

t=Thread(target=displaySeq('python')) # creation of thread 
t.start()


for j in range(10):
    print('Main value is',j)