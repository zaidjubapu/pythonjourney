import random
print("SNAKE WATER AND GUN")
d=0
l=0
w=0
i=0
r=10
while i < 10:
    inp=input("enter snake,water or gun :")
    gam=["snake","water","gun"]
    com=random.choice(gam)
    print("you selected: ",inp)
    print("computer selected: ",com)
    if inp==com:
        d=d+1
        r=r-1
        i=i+1
        print("draw")
        print("you have",r,"more games")
    elif inp=="snake" and com=="water" :
        w=w+1
        r=r-1
        i=i+1
        print("you won")
        print("you have",r,"more games")
    elif inp=="snake" and com=="gun":
        l=l+1
        r=r-1
        i=i+1
        print("you loss")
        print("you have",r,"more games")
    elif inp=="water" and com=="snake":
        l=l+1
        r=r-1
        i=i+1
        print("you loss")
        print("you have",r,"more games")
    elif inp == "water" and com == "gun":
        w = w + 1
        r = r - 1
        i = i + 1
        print("you won")
        print("you have", r, "more games")
    elif inp == "gun" and com == "snake":
        w = w + 1
        r = r - 1
        i = i + 1
        print("you won")
        print("you have", r, "more games")
    elif inp == "gun" and com == "water":
        l = l + 1
        r = r - 1
        i = i + 1
        print("you loss")
        print("you have", r, "more games")
    else:
        print("you have entered incorrect input")
print("you won: ",w)
print("you lost: ",l)
print("draw matches :",d)
if w>l:
    print("you have won the matched")
elif w<l:
    print("you lost the matched")
else:
    print("match draw")