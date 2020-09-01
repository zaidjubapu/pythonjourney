'''
global variable and local varible :
'''
'''l=5 # global variable which declared outside the function and can use any where but we cant change the globalvalue until global
# has used
def funct1(n):
    global l # to access the l value inside the function
    l=l+5# local variable whick declared inside the function And can use inside the function
            # it will run above eqn if l present inside the error if l not present inside
                # the variable then it wil throw an error so we use global keyword

    print(l,n) # it will goes first inside the function if the variable is not there then it will goes outside the
funct1("yes")
print(l) # now the l value will change '''
'''def zaid():
    x=20
    def shaihan():
        global x
        x=88
    print("before calling shaihan",x)# the 20 value will printed because it is outside the loop
    shaihan()
    print("after calling shaihan",x) # now also 20 value will be printed and if the global declared then also it will print 20
    # because it is inside his loop
zaid()
print(x)# now global value will be printed because it is out side the loop'''