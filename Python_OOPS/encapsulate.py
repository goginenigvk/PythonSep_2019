
#__variablename=value 
class Car: 
     __maxspeed=0 #int 
     __name='' #string 
     
     def __init__(self):
         self.__maxspeed=150
         self.__name='Audi'

     def drive(self):
       print(self.__maxspeed)
       Car.__show()
       obj=Car()
       obj.__instanceshow() # 

    
     @classmethod
     def __show(cls):
        print('in show methods')

     def __instanceshow(self):
         print('instanceshow')

     def longdrive(self,speed):
         self.__maxspeed=speed
         print(self.__maxspeed)
        

  
yellowcar=Car()
yellowcar.drive()
yellowcar.longdrive(180)

print(yellowcar._Car__maxspeed)

#objectreference._classname__privatemethod
#objectrefrence.publicaccess
yellowcar._Car__show()
Car._Car__show()

