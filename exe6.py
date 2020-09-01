import random
a=int(input("enter the  a no: "))
b=int(input("enter the b no: "))
c=random.randint(a,b)
print("player 1 turn")
d=int(input(f"please guess the no between {a} and {b} "))
i=1
while True:
    if d==c:
        print(f"correct you guess in {i} trials")
        break
    else:
        if d>c:
            print("Incorrect guses.... you have entered bigger no")
        else:
            print("Incorrect guses.... you have entered lesser no")
        d = int(input(f"please guess the no between {a} and {b} "))
        i=i+1
print("player 2 turn")
c=random.randint(a,b)
d = int(input(f"please guess the no between {a} and {b} "))
j=1
while True:
    if d==c:
        print(f"correct you guess in {j} trials")
        break
    else:
        if d > c:
            print("Incorrect guses.... you have entered bigger no")
        else:
            print("Incorrect guses.... you have entered lesser no")
        d = int(input(f"please guess the no between {a} and {b} "))
        j=j+1
if i>j:
    print("player 1 trials",i)
    print("player 2 trials", j)
    print('player 2 wins')
elif i <j:
    print("player 1 trials", i)
    print("player 2 trials", j)
    print("player 1 wins")
else:
    print("player 1 trials", i)
    print("player 2 trials", j)
    print("tie")


