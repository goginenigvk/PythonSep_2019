filea=open('files/appendfile.txt','r')
if filea.writable():
    filea.write("hello ... how are you ...")
    filea.write(" i am appending some text to the file")
    filea.writeline("ll")
else:
   print("it is not in write mode")

filea.close()

# with - key word 