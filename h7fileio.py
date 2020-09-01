'''
      # more on files function
f=open("zaid.txt")
print(f.tell()) #to tell where the pointer is located
print(f.readline())
print(f.tell())
f.seek(30) # we can adjust the pointer by using seekfunctons
print(f.tell())
print(f.readline())
f.seek(20)
print(f.readlines())
f.close()'''
                     #opening file with block function
'''with open("zaid.txt") as f: # new way to open file and here we dont need to close a file because  it wil in default
    print(f.readlines())

z=open("zaid.txt")
print(z.readline())'''

# f=input("enter the file name : ")
z=open("akd",'w')
print(z)
z.close()