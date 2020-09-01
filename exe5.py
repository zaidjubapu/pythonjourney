'''def pattern(n):
    k=n-1
    for i in range(n):
        for j in range(k):
            print(" ",end="")
        k=k-1
        for l in range(0,i+1):
            print("*",end=" ")
        print()
pattern(4)''' # pattern printing
x=[int(x) for x in (input("enter the inputs by space")).split(" ")]
# x=[23,18,5,45]
def palindrome(x):
    z=[]
    for i in x:
        if i <= 10:
            z.append(i)
        else:
            a=str(i)
            a=a[::-1]
            if i == int(a):
                z.append(i)
            else:
                while True:
                    i=i+1
                    a = str(i)
                    a = a[::-1]
                    if i == int(a):
                        z.append(i)
                        break
    return z
print(palindrome(x))



