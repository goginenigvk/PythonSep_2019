def display_name(pname,page=27):
    name=pname
    print(name,page)


display_name('Raja')
display_name('Rahul')
display_name('Sachin')


def disply_person(name,age):
    print(name,age)


disply_person(19,'Rahul')


def display_list(listx):
    for i in listx:
        print(i)

display_list([1,6,8,9])


def display_dict(dictval):
    for i in dictval.items():
        print(i)

display_dict({'one':1,'two':2})
