import time
def countdown(num):
    print('count down starting ....')
    while num > 0:
        yield num
        num=num-1

countvalue =countdown(5)
for x in countvalue:
    print(x)
    time.sleep(2)