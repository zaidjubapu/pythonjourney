'''map filter and reduce:
numbers=["1","2","3","4"]
for i in numbers:
    i=int(i)
    print(i+3)

    # or
numbers=["1","2","3","4"]
for i in range(len(numbers)):
    numbers[i]=int(numbers[i])
print(numbers[2]+3)

# to do this in one line so we use map function
numbers=["1","2","3","4"]
print(map(int,numbers)) # it wiil print the address.. so that address should convert in list so we write
num=list(map(int,numbers))
print(num) # it will give in list as well as in integer form'''

# map function is used for other purpose
'''num=[1,2,4,5,6] # if we want square of this
def sq(a):
    return a*a
squares=list(map(sq,num)) # it will give square of all the num variable
print(squares)'''

'''# by using lambda function
num=[1,2,4,5,6]
square=list(map(lambda num:num*num,num)) # the first arg of the map should be the function and the sec arg should iterable
#square=list(map(num,lambda num:num*num)) # error thea 0bject is not iterable
print(square)'''
''' similar but tricky
def sq(a):
    return a*a
def cub(a):
    return a*a*a
func=[sq,cub]
def sum(a):
    return a+a
def minus(a):
    return a-a
func1=[sum,minus]
for i in range(5):
    v=list(map(lambda x,y:x(i)+y(i),func,func1)) # func and func1 are iterable and func and 
    # func1 value will passed to x,y respectively hence it operates
    print(v)'''
# use of filter function
'''a=[1,2,3,4,5,5,6,7,8]
def isgreater(num):
    return True
z=list(filter(isgreater,a)) # first arg must be an funct in both map as well as in filter and the second arg 
# must be iterable and must give value so in filter the first arg is true then the value of a is passied in zaid
print(z)'''

# reduce function
'''
Reduce: it is function from functools so we should import from functools
if we want to add the items from the list then we can use it. in single line we can code
'''
from functools import reduce
list1=[1,2,3,4,5,6]
p=reduce(lambda x,y:x+y,list1) # it will take the list1 values and pass it tothe lambda function
print(p)
