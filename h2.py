'''
list and list functions:
list=[4,3,3,2,2,10]
z=list.sort()
print(z) # if we print z here then it will not give output shows none
# if we print list.sort() then only it will give output because list is mutable

dictionary and its function:
d1={"zaid":"burger","mohammed":"4",4:5,"hello":{"b":"maggie","l":"roti","d":"mango"}} # SYNTAX {keys:values}
print(d1.keys())
print(d1.values())
print(d1["hello"])# it wil print all dictionary
print(d1["hello"]["l"]) # it will print roti
d1["hasan"]=['hello'] # it will add hasan in dict
print(d1)
del d1['hasan']# it will remove hasan from dict
print(d1)

d2=d1
del d2["zaid"]
print(d1) # it will delete the value of zaid from d1 so we use copy functions

d2=d1.copy()
del d2["mohammed"]
print(d1)# it will not dlt from d1

print(d1.get("mohammed")) # it will give value of mohammed

d1.update({"hussain":"abcul"})
print(d1) # it will add this in dict'''

'''
create a dict and take input from user and the return  the meaning of that input

dict={"set":"its a collection of well define object","mutable":"we can change","immutable":"we cant change","zaid":"yeah iam zaid"}
inp=input("enter the word: ")
if inp=="set":
    print(dict[set])
elif inp=="mutable":
    print(dict["mutable"])
elif inp=="immutable":
    print(dict["immutable"])
elif inp=="zaid":
    print(dict["zaid"])
else:
    print("you have entered incorrect word")'''
                                            #       else another code


'''dict={"set":"its a collection of well define object","mutable":"we can change","immutable":"we cant change","zaid":"yeah iam zaid"}
inp=input("enter a word")
print(dict[inp])'''

                               # for loop
'''

list1=[["harry",1],["larry",2],["zarry",3]] #list inside list
dict1=dict(list1) #convertting list to dict
print(dict1) # it will print in term of dict
for item,no in dict1.items(): # items  is used to sepetate the key and values it will convert  in lisst
    print(item,no)
print(dict1.items())'''
'''
create a list print list item if item greater than 6 and check whether the item is numeric or not

list=["zaid44",33,22,3,43,23,32]
for item in list and item>6:
    if str(item).isnumeric(): # is numeric is an attribute of string 
        print(item)'''

'''
excercise two :
create a faulty calculator if user input is 45*3=then the answer should be wrong that is 555 similarly 56+9=77 and 56/7

a=int(input("enter the first no: "))
b=input("enter the operator : ")
c=int(input("enter the second no: "))
if b=="+":
    z=a+c
    if (a==56 and c==9) or (c==56 and a==9):
        print(77)
    else:
        print(z)
elif b=="-":
    z=a-c
    if (a==56 and c==9) or (c==56 and a==9):
        print(77)
    else:
        print(z)
elif b=="*":
    z=a*c
    if (a==45 and c==3) or (c==45 and a==3):
        print(555)
    else:
        print(z)
elif b=="/":
    z=a/c
    if (a==56 and c==7) or (c==7 and a==56):
        print(4)
    else:
        print(z)
else:
    print("you have entered invalid input")'''
