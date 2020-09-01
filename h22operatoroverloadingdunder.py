class Employees:
    no_of_l=8
    def __init__(self,aname,asalary):
        self.name=aname
        self.salary=asalary
    def printdetails(self):
        return f"Namae is {self.name}. salary is {self.salary}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_l=newleaves
    def __add__(self, other):
        return self.salary+other.salary
    def __repr__(self):
        return self.printdetails()
    def __str__(self):
        return self.printdetails()

harry=Employees("harry",500)
larry=Employees("zaid",600)
print(harry+larry) # it will run untill dunder method is created

# run of repr method
print(harry) # to run this type of method we create repr method

# run of str method: automatically it will run str method untill it will not define be repr
print(harry) # it wil run str method
print(str(harry)) # this also run str method.. if str mthod is not there then also this eqn will run
print(repr(harry)) # it wil run repr method

