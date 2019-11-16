

f=open('Files/readme.txt','a+')

if f.readable(): #true/false 
    readdata= f.read()
    print(readdata)

    fileposition=f.tell()
    print('File location :',fileposition)

    changefilepostion=f.seek(2)
    print('changefilepostion ' ,changefilepostion)

    print('file new seek position before ', changefilepostion)

    f.write("seek postion at zero")
    print('file new seek position after ', fileposition)
   


    f.close()

else: #false 
    print('file is not defined in right mode')
