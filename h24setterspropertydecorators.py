'''# property
class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.email=f"{fname}.{lname}@gmail.com"
    @property
    def emails(self):
        return f"{self.fname}.{self.lname}@gmail.com"
    def explain(self):
        return f"this employee is {self.fname} {self.lname}"
harry=Employee("zaid","jubaapu")
larry=Employee("mohammed",'Zaid')
print(harry.email) # now if i want to change the fname from email we cant use this method that is
                   # self.fname=zain
                    # it will change the variable but it will not change from email because it will execute before
                    # so for this we use propery method
harry.fname="Zain" # now it will change the fname in emails function not in self.email
# print(harry.emails())
print(harry.emails)# beside emaail we use paranthesis because it is a function. so remove that paranthaesis we
                        # use property'''

# setters
'''class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@gmail.com"
    @property
    def emails(self):
        return f"{self.fname}.{self.lname}@gmail.com"
    def explain(self):
        return f"this employee is {self.fname} {self.lname}"
    @emails.setter # we use the function name before the dot .
    def emai(self,string):
        print('Setting now...')
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname = names.split(".")[1]

harry=Employee("zaid","jubaapu")
larry=Employee("mohammed",'Zaid')
print(harry.emails)
harry.emai="this.that@gmail.com" # to write this we use a function called setter
print(harry.emails) # now the value of fname and lname will change of the emails function'''

# now i want to dlt the attribute of email so i want to create an deleter
class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@gmail.com"
    @property
    def emails(self):
        return f"{self.fname}.{self.lname}@gmail.com"
    def explain(self):
        return f"this employee is {self.fname} {self.lname}"
    @emails.setter # we use the function name before the dot .
    def emai(self,string):
        print('Setting now...')
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname = names.split(".")[1]
    @emails.deleter
    def ema(self):
        self.fname="none"
        self.lname="none"

harry=Employee("zaid","jubaapu")
larry=Employee("mohammed",'Zaid')
print(harry.emails)
harry.emai="this.that@gmail.com"
print(harry.emails)
del harry.ema
print(harry.emails)
print(larry.emails)
del larry.ema
print(larry.explain())


