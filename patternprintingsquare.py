'''
star pattern printing:
inp=int(input())
for i in range(inp):
    print("*"*inp)
    inp-=1'''
inp=int((input("enter the no")))
if inp>0:
    print(" "+"*"*inp)
    for i in range(inp):
        print("*"+(" "*inp)+"*")
    print(" "+"*"*inp)
else:
    print("invalid inp")


