'''instance and class variable'
class Employees:
    zaid=8 # it is class varible

harry=Employees()
rohan=Employees()
harry.name="harry" # this is in instance variable which is made by harry
harry.salary="455"
rohan.role="instructor"
# if we want to change the class variable then we can change from class name itself not with object name
harry.zaid=9
print(harry.zaid) # it wil make a new instance variable which give 9 for only harry
print(rohan.zaid) # it will print 8 because the class varialble will not change from the objects
Employees.zaid=10
print(rohan.zaid) # it wil change the zaid value because class name has used
# if we want all harry variables in dictionary theen we used
a=harry.__dict__  # it wil give in dictonary form
print(a)'''
# self and__init__constructor
'''
ex:

class Employees:
    def printdetails(self):
        return f"Namae is {self.name}. salary is {self.salary}"

rohan=Employees()
harry=Employees()
rohan.salary=400
harry.salary=500
rohan.name="rohan"
harry.name="harry"
print(rohan.printdetails())'''

# creating an constructor
'''class Employees:
    def __init__(self,aname,asalary):
        self.name=aname
        self.salary=asalary
    def printdetails(self):
        return f"Namae is {self.name}. salary is {self.salary}"
harry=Employees("harry",450) # class will not take argument unless the constructor is not created
# rohan=Employees()
# print(harry.name) # it will print harry which we have give the arguments
# if so for shortcut to make this we use constructor
# rohan.salary=400
# harry.salary=500
# rohan.name="rohan"
# harry.name="harry"
print(harry.printdetails())
print(harry.name)'''
 # class method: used to change the class variable
'''class Employees:
    no_of_l=8
    def __init__(self,aname,asalary):
        self.name=aname
        self.salary=asalary
    def printdetails(self):
        return f"Namae is {self.name}. salary is {self.salary}c"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_l=newleaves
harry=Employees("harr",500)
rohan=Employees("rohan",600)
rohan.change_leaves(34) # it will change the class variable
print(harry.no_of_l)'''
# creating an alternative class constructor using class method
'''class Employees:
    no_of_l=8
    def __init__(self,aname,asalary):
        self.name=aname
        self.salary=asalary
    def printdetails(self):
        return f"Namae is {self.name}. salary is {self.salary}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_l=newleaves
    @classmethod # alternative constructor using class mehtod
    def from_dash(cls,string):
        # params=string.split("-")
        # print(params)
        # return cls(100,500)
        # return cls(params[0],params[1])
        # to return in one line
        return cls(*string.split("-"))



harry=Employees("harr",500)
rohan=Employees("rohan",600)
zaid=Employees.from_dash("zaid-500")
print(zaid.salary)
# print(zaid.no_of_l)
# print(zaid.salary)'''

# static method in python
'''class Employees:
    no_of_l=8
    def __init__(self,aname,asalary):
        self.name=aname
        self.salary=asalary
    def printdetails(self):
        return f"Namae is {self.name}. salary is {self.salary}"
    @staticmethod # used as function without self and cls
    def hello(string):
        print("iam"+string)
harry=Employees("harr",500)
rohan=Employees("rohan",600)
rohan.printdetails()
rohan.hello("zaid")'''




