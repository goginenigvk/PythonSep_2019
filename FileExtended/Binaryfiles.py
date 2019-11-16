


filereader=open('FileExtended/readme.txt')
try:
   print(filereader.read())

finally:
    filereader.close()


with open('FileExtended/readme.txt')  as filereader:
    print(filereader.read())


with open('FileExtended/readme.txt','rb') as fr:
    print(fr.read())
 