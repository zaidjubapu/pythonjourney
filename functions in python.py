'''
there are two types :
buil in and user define
built in functIon:
        the function which are in build in python ex:
a=5
b=10
print(sum((a,b))) # sum is an in built function which can be seen by clicking on it that is ctrl button and click on sum

def function1(a,b):

    average=(a+b)/2
    sum=a+b
    return (sum) #it wil return the sum value to the functon1 and here the functoion will exit
    #print(average)
    return average # it will not run because it is in second
    
    print(sum)
v=function1(5,7)
print(v)'''

'''
docstring: this is comment which we write in the first line of the functoion'''
def function1(a,b):
    ''' this is function whick will give average of the two no'''
    average=(a+b)/2
    sum=a+b
    print(sum)
    return (sum,average) #will retuern sum and average value in functon1
print(function1(5,5))
print(function1.__doc__) # if we want doc string

