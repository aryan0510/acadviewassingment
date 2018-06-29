#1
'''
def calarea(r):
    pi=3.141
    are=(pi*(r**2))
    return are


y=float(input('enter the radius of circle'))
x= calarea(y)
print("area: ",x)
      

#2
def perfect(n):
    summ=1
    i=2
    while(i*i<=n):
        if n%i==0:
            summ=summ+i+n/i
        i+=1
        return(True if summ==n and n!=1 else False)
print("below are all perfect numbers")
n=2
for n in range(1000):
    if perfect(n):
        print(n)


#3
def multiply(n,i=1):
    print(n*i)
    if(i==10):
        return (1)
    else:
        multiply(n,i+1)
multiply(12)
'''


#4
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))

