# from abc import ABCMeta,abstractmethod
# class shape(metaclass=ABCMeta):
# or
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class Rectangle(shape):
    type= "Rectangle"
    sides=4
    def __init__(self):
        self.length=6
        self.b=7

    # def printarea(self):
    #     return self.length+self.b
harry=Rectangle() # if we use abstract method before any function. then if we inherit the class then it gives an errr
# untill that method is not created inside that class
#  now it wil give error
# we cant create an object of abstract base class method
