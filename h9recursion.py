'''
recursive and iterative method;
factorial using iterative method:

# using iterative method
def factorialiterative(n):
    fac=1
    for i in range(n):
        print(i)
        fac=fac*(i+1)
    return fac
# recusion method which mean callingthe function inside the function
def factorialrecursion(n):
    if n==1:
        return 1
    else:
        z= n * factorialrecursion(n-1)
        return z
n=int(input("enter the fact n0"))
print("the factorial iteration is", factorialiterative(n))
print("the factorial recursion is", factorialrecursion(n))
print(factorialrecursion(3))'''

# fibonaccis series:0 1 1 2 3 5 8 13 which adding the backwaard two numbers


'''
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    elif n==3: # if we want 3 addition
        return 1
    return fibonacci(n-1) + fibonacci(n-2)# + fibonacci(n-3) if we want 3 addition in line
n=int(input("enter the nuber"))
print(fibonacci(n))'''

def factorialrecursion(n):
    if n==1:
        return 1
    else:
        z= n + factorialrecursion(n-1)
        return z
n=int(input("enter the fact n0"))
print("the factorial iteration is", factorialrecursion(n))