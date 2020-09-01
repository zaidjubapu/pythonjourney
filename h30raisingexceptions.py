#raise: it is nothing but raising the error in python and furtheer program will not proceed
'''
a= input("what is name ")
if a.isnumeric():
    raise Exception("no are not allowed") # a is no this error will shows'''
# ex:2
'''
a= input("enter thee name  ")
b=input("how much you earn")

if int(b)==0:
    raise Exception("b is zero stoops")
print(f"hello {a}")'''
#ex:3
'''
a=input("enter the name: ")
try:
    print(c)
except Exception as e:
    if a=="zaid":
        raise Exception("zaid is blocked")
    print("value error")'''
# ex4
a=input("enter the name: ")
try:
    print(a)
    if a=="zaid": # now the if the error will occur then it wil move ot except
        raise Exception("zaid is blocked")
except Exception as e:
    print("value error")
