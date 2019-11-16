
file=open('Files/withfile.txt','a')
file.write("hello how are you")
file.close()
if file.closed:
    print("file is closed")
else:
    print('file is not closed')


with open('Files/withfilenew.txt','a') as f:
    f.write('hellow .....i am with statement')

if f.closed:
      print("with file is closed")
else:
      print('with file is not closed')




