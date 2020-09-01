'''class Employees:
    no_of_l=8
    def __init__(self,aname,asalary):
        self.name=aname
        self.salary=asalary
    def printdetails(self):
        return f"Namae is {self.name}. salary is {self.salary}"
    @staticmethod # used as function without self and cls
    def hello(string):
        print("iam"+string)#
harry=Employees("harr",500)
rohan=Employees("rohan",600)
rohan.printdetails()
rohan.hello("zaid")

# single level inheritance
class programmer(Employees):
    no_of_l = 10

zaid=programmer("zaid",500)
print(zaid.no_of_l)
print(zaid.name)

#multiple inheritance
class player:
    games="cricket"
    def __init__(self,games,no):
        self.game=games
        self.no=no

class coolprogrammer(Employees,player): # it will move according to arrangement
    g=5
a=coolprogrammer("zaid",300)
print(a.g)
print(a.games)
print(a.printdetails())

# multilevel inheritance
class dad:
    basket_ball=1
class son(dad):
    dance=1
    def isdance(self):
        a=5
        return f"yes i dance{self.dance} {a} no of times"
class grandson(son):
    dance = 5
    a=3
    pary=son()

    def isdance(self,a):
        self.dance=10 # we can change the class variable
        print(a)
        return f"yes I dance"\
            f"yes I danc awesomly {self.dance}  no of times"
    def __init__(self,aname,age,salary):
        self.name=aname
        self.age=age
        self.salary=salary

dary=dad()
# pary=son()
cary=grandson("zaid",20,5000)
print(cary.isdance(5))
print(cary.dance)
print(cary.pary.dance)'''

# public private protected variables
class dad:
    bas=1
    dance=2 # public variable can access outside the class directly
    _b=5 # protected variable can access outside the only in python or else it should be access only in python
    __c=10 # private cannot access outside the class untill the use of the class name
class son(dad):
    __dance=1
    _c=8
    def isdance(self):
        a=5
        return f"yes i dance{self.__dance} {self._c} no of times"
class grandson(son):
    def idance(self):
        a=5
        return f"yes i dance{self.dance} {a} no of times"
    # print(__c)
    def d(self):
        a = 5
        print(self.basket_ball)
        print(self._b)
        return f"yes i dance{self.__dance} {a} no of times"
    dance = 5
    a=3

harry=dad()
larry=son()
parry=grandson()
print(larry.bas)
print(parry.idance())