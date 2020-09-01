'''
while loop
i=0
while i<45:
    print(i,end=",") # if  we want in single line
    i=i+1

using break and continue statement:

i=0 #printing the odd no from 0 to 50
while(True):
    if i%2 !=0 :
        print(i,+3end=",")
        i=i+1
    else:
        i=i+1
        continue
    if i>51:
        break


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



