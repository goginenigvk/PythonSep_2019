

def average(marks):
    assert len(marks) != 0, 'Enter atleats one subject marks'
    return sum(marks)/len(marks)

markslist=[90,80,56,78,60,66]
avg=average(markslist)
print(avg)

markslist1=[]
avg1=average(markslist1)
print(avg1)

