# excercise 4 pattern printing
'''print("enter the row in int")
r=int(input())
b=int(input("enter the no 0 or 1"))
if b == 1:
    for i in range(1,r+1):
        print("*" * i)
if b==0:
    for i in range(1,r+1):
        print("*" * (r+1-i))'''
        # or

'''print("enter the row in int")
r=int(input())
b=int(input("enter the no 0 or 1"))
if b == 1:
    for i in range(1,r+1):
        for j in range(1,i+1):
            print("*",end="")
        print()
if b ==0:
    for i in range(r,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print()'''

