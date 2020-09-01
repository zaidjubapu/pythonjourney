'''
decorators in python:
'''
'''def fun1():
    print("iam zaid")

fun2=fun1
del fun1
fun2()''' # it will give the output as same

'''def fun1(num):
    if num == 0:
        return print
    if num ==1:
        return int
a=fun1(1)
print(a) # the output willshown as class int'''
#ex:3
'''def executor(func):
    func("iam zaid")
executor(print)'''

# now decorator
def dec1(func1):
    def nowex():
        print("excuting now")
        func1()
        print("executed")
    return nowex
# def zaid():
#     print("iam zaid")
@dec1
def zaid():
    print("zaid is a good")
# zai=dec1(zaid) # so to use this sectance we have a shortcut which is used before the zaid function
zaid()
