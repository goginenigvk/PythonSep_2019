from threading import Thread

class Mythread(Thread):
    def run(self):
        for i in range(10):
            print('class thread - ',i)


t=Mythread()
t.start()

for j in range(10):
    print('main thread -',j)