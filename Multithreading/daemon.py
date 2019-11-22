
from threading import Thread

def job():
    print('job execution ......')

t=Thread(target=job)
#t.start()
print(t.is_alive()) # True/ False 
print(t.isDaemon()) # True/False 

t.setDaemon(True)
print(t.isDaemon())
t.start()
print(t.is_alive())