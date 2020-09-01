# file io basic
'''f = open("zaid.txt","rt")
content=f.read(10) # it will read only first 10 character of file
print(content)

content=f.read(10) # it will read next 10 character of the file
print(content
f.close()
 # must close the file in every program'''
'''f = open("zaid.txt","rt")
content=f.read() # it will read all the files
print(1,content) # print content with one

content=f.read()
print(2,content) # it will print only 2 because content are printed allready
f.close()'''

'''if we want to read the file in a loop with 
f = open("zaid.txt","rt")
for line in f:
    print(line,end="")'''
# if want to read character in line by line
'''f = open("zaid.txt","rt")
content=f.read()
for c in content:
    print(c)'''

#read line function
'''f = open("zaid.txt","rt")
print(f.readline()) # it wiil read a first line of the file
print(f.readline()) # it will read next line of the file it will give a space because the new line wil already exist in that
f.close()'''

# readlines functon wil use to create a list of a file with 1 line as 1 index
'''f = open("zaid.txt","rt")
print(f.readlines())'''
                # writ functions
'''f=open("zaid.txt","w")
f.write("hello how are you") # replce the content with  what we have written
f.close()'''

'''f=open("zaid1.txt","w") # the new file wil come with name zaid1
f.write("hello how are you") # the new file will created and the content will what we have written
f.close()'''
            # append mode in write
'''f=open("zaid2.txt","a") # the new file wil come with name zaid1 and will append the character at the end how much we run the program
a=f.write("hello how are you\n") # the new file will created and the content will what we have written
print(a) # it will display the no of character in the file
f.close()'''

                #if want to use read and write function simultaneously
f=open("zaid.txt","r+") #r+ is used for read and write
print(f.read())
f.write("thankyou")
f.write("zaid")
f.close()



