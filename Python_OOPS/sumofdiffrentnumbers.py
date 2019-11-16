class MultipleAddition:

       def sum(self,*numbers):
           total=''
           for num in numbers:
                total=total+num 
           print('Result is ',total)   

add=MultipleAddition()  
add.sum(1,'two')
add.sum('two','three','four')




 