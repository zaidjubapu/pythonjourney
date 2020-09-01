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
print(harry.email)


# object instropection
print(dir(harry))
print(id(harry))