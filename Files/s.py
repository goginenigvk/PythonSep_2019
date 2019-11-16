import os  

#Return the effective group id of the current process. 
# This corresponds to the “set id” bit on the file being executed in the current process.
#Availability: Unix
print(os.getgid())  #20

print(os.getlogin())

print(os.getcwd())

#Return the current process’s real user id 
#unix
print(os.getuid())
# print(os.path())
print(os.access('sample.txt',os.R_OK))
print(os.listdir())
print(os.lstat('/'))
#print(os.mkdir('hello'))

#print(os.mkfifo('hellowww'))

#print(os.rename('hello','hello1'))

print(os.rmdir('hello1'))