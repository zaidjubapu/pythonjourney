'''def function1():
    print("subscribe now")
func2=function1
del function1 # dlt the function
func2()'''

'''def function1(num):
    if num==0:
        return print
    if num==1:
        return int
a=function1(0)
print(a)''' # we can pass the function
'''def funcq(f):
    f("hell")
funcq(print) # we can pass the function as argument'''
'''def dec(func1):
    def nowexec():
         print("executing now")
         func1()
         print("executed")
    return nowexec()
@dec
def zaid():
    print("iam zaid")
# zaid=dec(zaid) # short cut of this is called decorator
zaid'''



