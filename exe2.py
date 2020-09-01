'''
Problem Statement:
Harry potter has got n number of apples. Harry has some students among whom, he wants to distribute the apples. These n number of apples are provided to harry by his friends and he can request for few more or few less apples.

You need to print whether a number in range mn to mx is a divisor of n or not.

Input:
Take input n, mn and mx from the user

Output:
Print whether the numbers between mn and mx are divisor of n or not. If mn = mx, show that this is not a range and mn is equal to mx. Show the result for that number

Example:
If n is 20 and mn=2 and mx = 5

2 is a divisor of 20

3 is not a divisor of 20

…

5 is a divisor of 20
'''
if __name__ == '__main__':
    a=int(input("enter the no of apples:"))
    b=int(input("enter the mn no: "))
    c=int(input("enter the mx no: "))
    if b==c:
        d=a%b
        if d == 0:
            print(b , "is divisor of ",a)
            print("it is not a range")
    else:
        for i in range(b,c+1):
            if a%i == 0:
                print(i,"is divsor of ",a)
            else:
                print(i," is not a divisor of ",a)