fileptr = open('Files/sample.txt','r')
if fileptr.readable():
     readfile= fileptr.readlines()
     print(readfile[0])

else:
    print('File is not readble mode')


fileptr.write("I am writing an article")

