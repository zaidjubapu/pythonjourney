
# *args:it is used to add the items in the function without using the variables
# ex:1

def funargs(*zaid):
    print(*zaid)
    print(zaid)
    for item in zaid:
        print(item,end=" ")
har=["zaid","zeeshan","shaihan"]
print(har)
print(*har)
funargs(*har)


# ex:2 with normal
'''
def funargs(normal,*zaid): # the normal will written before the * argument
    print(normal)
    for item in zaid:
        print(item,end=" ")
har=["zaid","zeeshan","shaihan"]
nor='the following students are: '
funargs(nor,*har)

ex:3 the kwargs argument

def funargs(normal,f,*zaid,**dic): # ** is used when dic is used
    print (normal)
    print(f)
    for item in zaid:
        print(item,end=" ")
    print("\nthe follwing are the: ")
    for key,values in dic.items():
        print(f"{key} is  a {values} boy")
har=["zaid","zeeshan","shaihan"]
nor='the following students are: '
kw={'zaid':"good","shaihan":"bad","zeeeshan":"basd"}
f=34
funargs(nor,f,*har,**kw) # it nust be written according to the order'''

