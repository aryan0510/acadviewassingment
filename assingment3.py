# 1
our_list = []
 
first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
third_num = int(input('Enter third number: '))

our_list.append(first_num)
our_list.append(second_num)
our_list.append(third_num)
 
print(our_list)

# 2
topcompanies_list =['google','apple','facebook','microsoft','tesla']
print(topcompanies_list)

# 3
our_list = [2,3,8,6,2,8,2,0,2]
print (our_list.count(2))

# 4
our_list = [2,3,8,6,2,8,2,0,2]
for item in our_list:
    item=int(item)
our_list.sort()
print (our_list)

# 5
A=[0, 2, 2, 2, 2, 3, 6, 8, 8]
B=[1,2,3,4,5,6,7,8,9]
C=[*A, *B]
C.sort()
print (C)

#6
stack = [1,2,3,4,5]
stack.append(5)
stack.append(9)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)


