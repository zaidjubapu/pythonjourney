'''
polymarphism : one thing in differnt form
ex:print(5+6)
print("5"+"6")
# no are same but forms are different
'''
# super and overriding
'''class A:
    classvar1='iam class variable a'
    c=5
    b=5
    def __init__(self,c):
        self.var1="iam inside class a constructor"
        self.classvar1="instance var in class A"
        self.z="z"
class B(A):
    classvar2="iam in class b"
    def __init__(self,c):
        self.var1="iam inside class b constructor"
        self.classvar2="instance var in class b"
a=A()
b=B()
print(b.classvar1) # it wil print instance var in class a , because it will move with instance variaable first then it will move to class variable
print(b.var1) #  it will print iam inside class b constructor if the methods name are same then the first method only it will initialize# to use the same method we use
# a function called super() the last method will be the final method 
# ex:2'''
'''class A:
    classvar1='iam class variable a'
    c=5
    b=5
    def __init__(self):
        self.var1="iam inside class a constructor"
        self.classvar1="instance var in class A"
        self.z="z"
class B(A):
    classvar2="iam in class b"
    def __init__(self):
        self.var1="iam inside class b constructor"
        self.classvar2="instance var in class b"
        super().__init__()
a=A()
b=B()
print(b.classvar1) # it wil print instance var in class a , because it will move with instance variaable first then it will move to class variable
print(b.var1) # now it will print iam inside class a constructor because of the last method'''