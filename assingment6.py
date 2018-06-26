#1
userinput=[]
for i in range(10):
    y=int(input("enter an integer"))
    userinput.append(y)
print("entered list",userinput)
    

#2
x=1
while x==1:
    print('hello')


#3
li=[]
for x in range(5):
    y=int(input("enter an integer value"))
    li.append(y)
print("entered list is:",li)
l2=[]
for x in li:
    z=x*x
    l2.append(z)
print("updated list is:",l2)


#4
l1=[2,3,'thor',7,'thanos',2.7]
l2=[]
l3=[]
l4=[]
for x in l1:
    if type(x)==int:
        l2.append(x)
for y in l1:
    if type(y)==str:
        l3.append(y)
for z in l1:
    if type (z)==float:
        l4.append(z)
print(l2)
print(l3)
print(l4)



#5
l1=[]
l2=[]
for x in range(1,101):
    if x%2==0:
        l1.append(x)
    else:
        l2.append(x)
print("even numbers:",l1)
print("odd numbers:",l2)


#6
for i in range(0,4):
    for j in range(0,i+1):
        print("* ",end="")
    print()

#7
d = {'one':1,'two':2,'three':3,'four':4}
for x in d.keys():
    print(x,d[x])

#8
userinput=[]
l1=[]
for i in range(5):
    y=int(input("enter an integer"))
    userinput.append(y)
x=int(input('enter the element you want to delete'))
for z in userinput:
      if z==x:
          userinput.remove(z)
      
print("the list is",userinput)
