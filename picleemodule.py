import pickle
# pickling a python object # cars is nothing but an object
'''cars=["audi:","cars","maruthisuxuki","volksf"]
file="mycar.pkl"
fileobj=open(file,"wb")  # it should be in write mode with binary
pickle.dump(cars,fileobj)''' # noe cars values will be dump at the filename mycar.pkl in binary mode
                            # dump method is used to dump the carsdata in fileobj

# to show in output which should use a method called load
cars=["audi:","cars","maruthisuxuki","volksf"]
file="mycar.pkl"
fileobj=open(file,"rb") # to read a file we usesd rb which will read in binary
a=pickle.load(fileobj) # load method will use to load the objedt preset in fileobj
print(a) # it will display what it has return
print(type(a)) # it will print class list