
from threading import Thread

class Task:
    def printtoptenvalues(self):
        for i in range(10):
            print('Task value -- ',i)
           
taskobj=Task()
t=Thread(target=taskobj.printtoptenvalues)
t.start()

for i in range(10):
    print('main thread --')

