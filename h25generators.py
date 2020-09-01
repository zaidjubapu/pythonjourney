'''
generotors:
the keyword is yield
its store the data in it and gives us output once at a time
and should be write within the function

ex:

def f1(n):
    for i in n:
        yield i

a=f1("hello")
print(a) # it will give generator object at some location
print(a.__next__()) # now it will print h
# we can use another method
print(next(a)) #now it print(e)'''
'''
list=[1,2,3,4]
iterable is items present in the list whether it is iterable or not it is nothing but iterable
# ex:str is iterable but int is not iterable
#list is iterable
# and iterotor is nothing but the variable namr now list has become an iterator
# and iteration is a process of moving one by one 
'''
# fibonacci series using  yield
def fac(n):
    if n==1:
        return 1
    for i in range(n):
        return n*fac(n-1)
a=fac(4)
print(a)
# a.__next__()
# fibonacci series using yield
def fibs(): # now fact will become an iterator will gives the value untill the funciton calls end
    a,b=0,1
    for i in range(20):
        yield a # yield is nothing but run one time in a loop untill it calls one more time
        # if the functioncalls one more time then it will runs from that loops itself
        # return a
        print(a,b)
        a,b=b,a+b
        print(a,b)
    for i in range(3):
        print(3)
for x in fibs(): # fact is an iterator yield a gives the values to the fact
    if x>50:
        break
    print(x)
# a=fibs()
# print(a.__next__()) # it will go one by one
# for i in range(5):
#     yield i # we cant write here because it is outside the function

