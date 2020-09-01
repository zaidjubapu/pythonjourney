'''
comprehensation
'''
'''
ls=[]
for i in range(100):
    if i%3==0:
        ls.append(i)
print(ls)
# to do this is one line is nothing but list comprehensation
ls=[i for i in range(100) if i%3==0]
    # before first space we can write variable that is i value and after first space loop and after second space conditon
print(ls)
a=[int(x) for x in input("enter the no").split()] # first it will take input and then it will split and form a list
# so that it will become  an iterator and then it will pass the value to the first that is int(x)
z=len(a)
print(a)
print(z)
# a=input("enter the no").split() # alternative
# print(a)'''

# dic comprehensation
'''
dict11={i:f"item {i}" for i in range(100)}
dict12={value:key for key,value in dict11.items() } # to do opposite in dictionary
print(dict11)
print(dict12)'''
# set comprehensation
'''
set1={i for i in [1,2,34,1,2,43,34,5]} # set will not repeat the variables
print(type(set1)) # it is set
l=[i for i in [1,2,34,1,2,43,34,5]]# set will not repeat the variables
print(type(l)) # it will list'''
# generator comprehensation we used paranthesis without using yield
'''evens=(i for i in range(100) if i%2==0)
print(type(evens))
print(evens.__next__()) # now even become an iterator
# if i want to run all then we used for loops which automatically runs till the end
for i in evens:
    print(i) # it will print all
a=[1,2,3,4]
print(a.iter(a))'''
# task
'''
we want to take the input how much item we want in the list
and ask user to write the nos
ask user which type of comprehensation you want and gives the output
'''
while(True):
    n=int(input("enter the no's of items : "))
    li=input("enter the items seperated by space: ")
    lis=li.split()
    le=len(lis)
    if le == n:
        while(True):
            com=(input("enter which comprehensation do you want 1 for list comprehensation"
                      " 2 for dict com"
                      " 3 for set com : "))
            if com=="1":
                s=[i for i in lis]
                print(s)
                print(type(s))
                break
            elif com=="2":
                s=[i for i in lis]
                print(s)
                print(type(s))
                break
            elif com=="3":
                s=[i for i in lis]
                print(s)
                print(type(s))
                break
            else:
                print("invalid input")
                continue
    else:
        print("you have  entered incorrect inputs")
        continue
    break









