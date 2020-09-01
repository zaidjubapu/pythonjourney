'''
string formattig:'''
'''ex:1
me ="zaid"
z=3
a="this is %s"%(me,z)
print(a)'''

'''ex2:
me="zaid"
z=3
a="this is {} {}"
b=a.format(me,z)
print(a)
print(b)# output:this is 3 zaid

me="zaid"
z=3
a="this is {1} {0}"
b=a.format(me,z)
print(a)
print(b) # output:this is 3 zaid'''

'''ex:3 updated version and convinient'''
me="zaid"
a=3
b=f"this is {a} {me}"# easy way of formatting the string
print(b) #0utput theis is 3 zaid