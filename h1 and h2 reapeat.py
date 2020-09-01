a="mohammed zaid"
print(a[10:len(a):2]) #reversing the string

z="jkafjafs72758d"
print(z.isalnum()) #if there is space we wil get false else true now output is true'''

z="mynamc5345334hd"
print(z.isalpha()) #if there is space we wil get false else true if there is only alphabets.. now false because it has both

z="hello iam zaid"
print(z.endswith("zaid")) # it is true because the string ends with boy and its string functions

z="hello iam zaid"
print(z.find("zaid")) # it wil give out as 10 because at 10 index z is started

d1={"zaid":"burger","mohammed":"4",4:5,"hello":{"b":"maggie","l":"roti","d":"mango"}} # SYNTAX {keys:values}
print(d1.keys())
print(d1.values())
print(d1["zaid"])
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
