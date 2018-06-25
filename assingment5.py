#1

n=int(input('enter year'))
if((n%4)==0):
    if((n%100)==0):
        if((n%400)==0):
            print('leap year')
        else:
                print('normal year')
    else:
        print('leap year')
else:
    print('normal year')


#2
length=int(input('enter length of figure'))
breadth=int(input('enter breadth of figure'))
if length== breadth:
    print('this is a square')
else:
    print('this is a rectangle')


#3
p1=int(input('enter age of first person'))
p2=int(input('enter age of second person'))
p3=int(input('enter age of third person'))
if (p1>p2) and (p1>p3):
    print('p1 is older')
else:
    print('p1 is younger')
if (p2>p1) and (p2>p3):
    print('p2 is older')
else:
    print('p2 is younger')
if(p3>p1) and (p3>p2):
    print('p3 is older')
else:
    print('pe is younger')


#4
points=int(input('enter points obtained'))
if (points>=1) and (points<=50):
    print('no prize')
elif (points>=51) and (points<=150):
    print('you have won a wooden dog')
elif (points>=151) and (points<=180):
    print('you have won a book')
elif (points>=181) and (points<=200):
    print('you have won choclates')




#5
pur=int(input('enter price of total purchased'))
if (pur>1000):
    a=pur/10
    finalpri=pur-a
    print(finalpri)
else:
    print('you have no discount')
