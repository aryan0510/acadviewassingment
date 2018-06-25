
#1
tuple=(0,1,2,3,4,5,6,7)
print(len(tuple))


#2
tuple=(1,2,3,4,5,6,7)
print(max(tuple))
print(min(tuple))


#3
from functools import reduce
reduce(lambda x, y: x*y,[1,2,3,4,5,6])


#4
setx=set(["green","blue"])
sety=set(["blue","yellow"])
setz=setx & sety
print(setz)
setb=setx-sety
print(setb)
seta=setx|sety
print(seta)


#5
mydict={}
for i in range(10):
    name=input('enter student name')
    marks=input('enter marks of student')
    mydict[name]=marks
    print(mydict)



