

class Customer:

    def __init__(self,name,accounttype,amount):
        self.name=name
        self.accounttype=accounttype 
        self.amount=amount 

    
    def customerdetails(self):
        print(self.name)
        print(self.accounttype)
        print(self.amount)


class Transaction:
    
    @staticmethod
    def deposit(cus,amountdeposit):
        cus.amount=cus.amount+amountdeposit
        cus.customerdetails()


cobjref=Customer('John','SavingsAccount',2000)
Transaction.deposit(cobjref,1000)