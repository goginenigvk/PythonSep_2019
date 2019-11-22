
from threading import Thread,current_thread,active_count
import time

def displayThread():
    print(current_thread().name,'.....started')
    time.sleep(1)
    print(current_thread().name,'......ended')


print('Number of active threads- before thread call',active_count())
t1=Thread(target=displayThread,name='Thread1')
t2=Thread(target=displayThread,name='Thread2')
t3=Thread(target=displayThread,name='Thread3')
t1.start()
t2.start()
t3.start()

print('Number of active threads - after thread call',active_count())
time.sleep(10)
print('Number of active threads - final call',active_count())


