import os
print(os.getcwd()) # it will get the  location of the system
# cwd= current working directory is important if we want to open any file it will check in curent working directory
# if not found it will give us error. below is the example
# if  i want to change the location of the system
# os.chdir("c://")
# print(os.getcwd())
# f=open("zaid.txt") # now it will not get the file
# if i want all files of a directory
print(os.listdir()) # it will give all the files inside this directary
print(os.listdir("c://")) # it will shows aall the files located in c directoray
# to create an folder in the directary
os.mkdir("hello")
# to create multiple files
os.mkdir("zaid/zain") # now it will create zaid zain files
