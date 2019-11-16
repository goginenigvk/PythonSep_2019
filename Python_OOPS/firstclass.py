


class Customer:
    ''' This class is defined customer information 1''' #docstring

    # constructor  - Variables 
    def __init__(self,name,id,location): #('rahul')
        self.customername=name
        self.customerid=id
        self.customerlocation=location

    #method - 
    def customer_deposit(self):
        print(' Customer deposit deatils')
        print()
        print('customer name',self.customername)
        print('customer id',self.customerid)
        print('customer location',self.customerlocation)

    def customer_withdraw(self,amount):
        print(' Customer withdraw deatils')
        print()
        print('customer name',self.customername)
        print('customer id',self.customerid)
        print('customer location',self.customerlocation)
        print('amount is ',amount)



Rahulcustomer=Customer('Rahul','A12345','Bangalore') # 
Johncustomer=Customer('John','B12345','Chennai') # 

Rahulcustomer.customer_deposit()
Johncustomer.customer_deposit()
Johncustomer.customer_withdraw(5000)



    




