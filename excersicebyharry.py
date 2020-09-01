# health management system
'''inp=(int(input("enter 1 as harry, 2 as zaid, 3 as zeeshan")))
inp1=(int(input("enter 1 for diet, 0 for fitness")))
def gettime():
    import datetime
    return datetime.datetime.now()
if inp==1 and inp1==1:
    with open("harrydiet") as f:
        print(gettime(),"\n", f.read())
elif inp==1 and inp1==0:
    with open("harryfit") as f:
        print(gettime(), f.read())
elif inp==2 and inp1==1:
    with open("zaiddiet") as f:
        print(gettime(), f.read())
elif inp==2 and inp1==0:
    with open("zaidfit") as f:
        print(gettime(), f.read())
elif inp==3 and inp1==1:
    with open("zeeshandiet") as f:
        print(gettime(), f.read())
elif inp==3 and inp1==0:
    with open("zeeshanfit") as f:
        print(gettime(), f.read())
else:
    print("you have entered incorrect input")

# management system by harry
i=int(input("enter 1 for harry 2 for zaid 3 for zeeshan\n"))
i1=int(input("enter 1 for diet 2 for fitness\n"))
i2=int(input("enter 1 for add 2 for retrive\n"))
def getdate():
    import datetime
    return datetime.datetime.now()
if i == 1 and i1==1 and i2==1:
    item=input("add the items")
    with open("harrydiet","a") as f:
        a=f.write("you have eaten at "+ str(getdate())+": "+ str(item)+"\n")
elif i == 2 and i1==1 and i2==1:
    item = input("add the items")
    with open("zaiddiet","a") as f:
        a=f.write("you have eaten at "+ str(getdate())+ ": "+str(item)+"\n")
elif i == 3 and i1==1 and i2==1:
    item = input("add the items")
    with open("zeeshandiet","a") as f:
        a=f.write("you have eaten at "+ str(getdate())+": "+ str(item)+"\n")
elif i == 1 and i1==2 and i2==1:
    item = input("add the items")
    with open("harryfit","a") as f:
        a=f.write("excercise done at "+ str(getdate())+":"+ strt(item)+"\n")
elif i == 2 and i1==2 and i2==1:
    item = input("add the items")
    with open("zaidfit","a") as f:
        a=f.write("excercise done at "+ str(getdate())+": " +str(item)+"\n")
elif i == 3 and i1==2 and i2==1:
    item = input("add the items")
    with open("zeeshanfit","a") as f:
        a=f.write("excercise done at "+ str(getdate())+ ": "+ str(item)+"\n")
elif i==1 and i1==1 and i2==2:
    with open("harrydiet") as f:
        a=f.read()
        print(a,"\n thankyou")
elif i==2 and i1==1 and i2==2:
    with open("zaiddiet") as f:
        a=f.read()
        print(a, "\n thankyou")
elif i==3 and i1==1 and i2==2:
    with open("zeeshandiet") as f:
        a=f.read()
        print(a, "\n thankyou")
elif i==1 and i1==2 and i2==2:
    with open("harryfit") as f:
        a=f.read()
        print(a, "\n thankyou")
elif i==2 and i1==2 and i2==2:
    with open("zaidfit") as f:
        a=f.read()
        print(a, "\n thankyou")
elif i==3 and i1==2 and i2==2:
    with open("zeeshanfit") as f:
        a=f.read()
        print(a, "\n thankyou")

excersice three:
guessing the no:
n=20
print("you have totally 9 guesses")
print("no is beteween 1 to 100")
i=1
z=9
while(i<10):
    inp=int(input("enter a no\n"))
    if inp == n:
        print("you won")
        print("you have taken only" ,i ," guess to finish")
        break
    elif inp<n:
        print("you entered less no")
        z=z-1
        print("you left with" , z , "guesses")
        i=i+1
    elif inp>n:
        print("you entered MORE no")
        z=z-1
        print("you left with ", z ," guesses")
        i=i+1
if z==0:
    print("you lost")'''