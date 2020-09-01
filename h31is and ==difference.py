# ==: value equality :if the objects value are equal then it will gives true
# is: refrence equality if the objects location are equal then it will return true
# ex:1
'''
a=[1,2,3,4]
b=a
if b==a:
    print("true") # now it will print true because both have same values
else:
    print("false")

if b is a:
    print("yes b is a") #now this wil print because it has poin on same location
else:
    print("no it has different locations")'''
# ex:2
a=[1,2,3,4]
b=a.copy()
b=a[:] # another method of coping the string
if b==a:
    print("true") # it will print because it has same values
else:
    print("false")

if b is a:
    print("yes b is a")
else:
    print("no it has different locations") # now this will print because it point in different locations