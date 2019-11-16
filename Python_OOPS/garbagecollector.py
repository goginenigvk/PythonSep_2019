import time 
import gc 
class TestGarbageCollector: 
      def __init__(self):
          print('object creation')
      
      def __del__(self):
          print('Object deletion .....')



print(gc.isenabled())


objref=TestGarbageCollector()
gc.disable()
objref=None
del objref 


time.sleep(10)
print('Application closed')
