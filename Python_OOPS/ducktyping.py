class Duck: 
    def quack(self,name):
        print("Quacked")


class MallarDuck:
    def quack(delf):
        print("louder quacked")

class Eagle: 
    def fly(self):
        print('i just fly')


class MakeitQuack:
    def __init__(self,bird):
         bird.quack()
         bird.fly()



MakeitQuack(Duck())
MakeitQuack(MallarDuck())
MakeitQuack(Eagle())
