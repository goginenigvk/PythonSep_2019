
x=2 #global variable


def number(x):
    print(x)

#Instance (3) & Class (static)-

# Car 
# model, year,availble ,color, wheels, company, CEO, headquarter 

class Car:

    carname='MG' #class variable/ Static variable 
    
    def __init__(self,model,year,*availble,**branchhead):
        Car.companyCEO='William'  #class variable inside the constructor 
        self.model=model
        self.year=year
        self.availble=availble
        self.branchhead=branchhead
        print(x)
    

    def showCarDetails(self):
        Car.headquarter='London'
        self.color=['red','white','black'] #assigning the list to instance variable

        print('=======================')
        #print('car parenntcompany',Car.parentcompany)
        print('Car Company',Car.carname)
       # print('Car founders',Car.foundername)
        print('Car Company CEO',Car.companyCEO)
        print('Car Headquarter',Car.headquarter)
        print('Model ',self.model)
        #print('Car wheels',Car.wheels)
        print('year',self.year)
        print('available',self.availble)
        print('color',self.color)
        print('Brnach head info:')
        for branchloc,branchheadname in self.branchhead.items():
            print(branchloc,branchheadname)

    @classmethod
    def getCarFounders(cls):
        cls.foundername='Donald' #class inside the class method
        print(cls.carname)

    @staticmethod  
    def getProducerCars_2019(count):
        Car.parentcompany='XYZ'
        print(count)

       

c=Car('hector',2019,'INDIA','UK','CHINA',India_branch='John',UK_branch='Roy')

Car.wheels=4
c.showCarDetails()
Car.getCarFounders()

Car.getProducerCars_2019(20000)

print(Car.__dict__)
print(c.__dict__)



