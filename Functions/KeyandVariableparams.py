#Two type - spl arguments 

# *vargs  - Variable length arguments 
#variablevalue
# **Kwargs - Keyword arguments 
# variablename=variable value 

def names(*argv):
    for i in argv:
       print(i)

names('Raja','Rahul','Sachin')


def persondata(*pdata):
    x=list(pdata)
    print(x[2])

persondata('John',27,300.67)

def employeeinfo(name,*dept,**adress):
    for i in adress.values():
        print(i)
       
    print(name,*dept)

#employeeinfo('Raj','IT','admin','manager','comm=Hyd','Padd=Bang','age=27')
employeeinfo('Raj','IT','admin','manager','comm'== 'Hyd','Padd'=='Bang')
employeeinfo('Raj','IT','admin','manager',comm = 'Hyd',Padd='27')


