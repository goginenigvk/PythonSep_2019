

# instance /object variable 
# class / static variable 
#  local /method variable 

class Cutsomer: 

    bankname='DBS BANK' # static variable / Class level 
                        # only once class variable is being called
                        # outside of method and constructor

    def __init__(self,customername,accountnumber):
        firstnumber=3 #local/method variable 
        secondnumber=5 # local variable 
        result =firstnumber+secondnumber
        print(result)

        #instance variable in construtor  / Object level
        self.customername=customername
        self.accountnumber=accountnumber
        print('calling from constructor',Cutsomer.bankname)

    
    def displaycustomerinfo(self):
        firstnumber=3 #local/method variable 
        secondnumber=5 # local variable 
        result =firstnumber+secondnumber
        print(result)
        #instance variable  in instance method
        self.customerage=45
        print(self.customername)
    
        

cobjref=Cutsomer('John',534123)
cobjref2=Cutsomer('Rahul',12345)

#instance variable declartion outisde class
cobjref.customerlocation='Bangalore'


cobjref.displaycustomerinfo()
print(cobjref.customername) #to access the instance variable - object reference 


print(cobjref.__dict__) #display all instance variables
print(cobjref2.__dict__)

# classname.variablename
print(Cutsomer.bankname)
    



