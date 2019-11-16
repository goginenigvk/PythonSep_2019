import os

try:
    list1=[1,6,7,8,9,3]
    print("in try block")
    #os._exit(0)
    print(list1[6])

    dict2={"one":1,"two":2}
    print(dict2["three"])

except (IndexError,KeyError) as message:
    print("exception is raised",message,IndexError)

except ValueError:
    print("value error")
else:
    print("in else block")

finally:
    print("in finally block")







     
  


 

