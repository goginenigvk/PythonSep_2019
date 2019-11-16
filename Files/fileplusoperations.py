import os

#os.mkdir('newDIR')
#os.rename('newDIR','ExtraDIR')
#os.rmdir('ExtraDIR')
print('current working DIR',os.getcwd())
#os.chdir('')
print(os.listdir())
lisdirs=os.listdir()
for i in lisdirs:
    string=i
    print(string)

print(os.getgid())
print(os.getpid())
print(os.getppid())