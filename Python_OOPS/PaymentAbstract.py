from abc import ABC,abstractmethod
class PaymentGateway(ABC):  
      
      def __init__(self):
          print('abstract class constructor')

      def showpaymentdetails(self):
         print("payment information")
    
      @abstractmethod
      def payment(self,amount):
          pass

class CreditCardPayment(PaymentGateway):

     def payment(self,amount):
         print('Credit Card Payment',amount)


class MobilePayment(PaymentGateway):

      def payment(self,amout):
         print('Mobile payment',amout)

#p=PaymentGateway()
c=CreditCardPayment()
c.payment(2000)
c.showpaymentdetails()
