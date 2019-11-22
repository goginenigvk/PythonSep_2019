
import time 
from threading import Thread
def task1(numbers):
    for i in numbers:
        time.sleep(1)
        print('Double of numbers --',i*2)
    

def task2(numbers):
    for i in numbers:
        time.sleep(1)
        print('Square values --',i*i)

numbers=[1,2,3,4,5,6,7]

starttime=time.time()
# task1(numbers)
# task2(numbers)
t1=Thread(target=task1,args=(numbers,))
t2=Thread(target=task2,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
endtime=time.time()
print('Total time taken :', endtime-starttime)