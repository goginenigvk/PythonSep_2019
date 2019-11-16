
# instance method 
# class method 
# static method 

class Customer: 
   
    #instance variable 
    bankname='DBS Bank'  
    
    # constructor method
    def __init__(self,cname,caccountnumber):
        self.name=cname
        self.accountnumber=caccountnumber

    #instance method
    def displayCustomerInfo(self):
        print('Customer name',self.name)
        
    #class method
    @classmethod
    def getBankName(cls):
        print(cls.bankname)
    
    #static method 
    @staticmethod
    def getCustomerCount(n):
        print('count',n)

# Create a obj reference 
objref=Customer('John',12345)
#calling instance method 
objref.displayCustomerInfo()

# calling class method
Customer.getBankName()

#calling static method
Customer.getCustomerCount(1000)
objref.getCustomerCount(5000)


