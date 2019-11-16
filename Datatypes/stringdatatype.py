""" name="India"
name="INDIA"

name="INIDA ONE"
name2="hello"

print(name)
print(name[3])
print(name[1:5])

print(name*3)
#print(name*'hello')

print(name+name2)
#name2[2]='9'

for i in name2:
  print(i)

for j in range(5):
    print(j)
 """

countryname='The capital of India is New Delhi. Sachin is India  most famous crikekter'
print(countryname.capitalize())

print(countryname.casefold())
person1="john"
person2="JOHN"
print(person1, person2)

if person1.casefold()== person2.casefold():
    print("matched")
else:
    print("not matched")

print(countryname.center(56,'*'))
print(len(countryname))
print(countryname.count("D",7,18))

print(countryname.find("India1"))

text="def1"
print(text.isidentifier())

print(countryname.encode(encoding="UTF-8"))

print(countryname.lower())
print(countryname.upper())

text1="x"
text2="IND"
text3=text1.join(text2)
print(text3)

list1={"India",'Poland',"Italy"}
splchar=">>"
text4=splchar.join(list1)
print(text4)

print(text2.swapcase())

rev=text2[::-1]
print(rev)


content='OnePlus 7T Pro India launch teased on Amazon, launching on October 10'
print(content.title())


content2="hello"
x=len(content)
print(content.zfill(x+9))

print(content.index('xx'))
print(content.find('xx'))

