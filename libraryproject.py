class Library:
    def __init__(self,list):
        self.Books=list
        self.lendbook={}
    def Displaybooks(self):
        print("The books available are in shown below")
        for b in self.Books:
            print(b)
    def Addbook(self,book):
        self.Books.append(book)
        print("books is succefully added")
    try:
        def Lendbook(self,bookname,user):
            if bookname in self.Books:
                self.lendbook.update({bookname:user})
                self.Books.remove(bookname)
                print("thanks for taking the book")
            else:
                if bookname not in self.Books:
                    print("this book is not there in our library")
                if bookname in self.lendbook:
                    print("OOPS! the book has been taken by ", self.lendbook[bookname])
                    print("you can take the book which is available")
    except Exception as f:
        print(f," error")
    def Returnbook(self,returnbook):
        try:
            self.Books.append(returnbook)
            self.lendbook.pop(returnbook)
            print("Thankyou for returning the book")
        except Exception as d:
            print(d," error")

if __name__ == '__main__':
    Bhatkal = Library(["c", "c++", "java", "javascript", "python", "django"])
    print(Bhatkal)
    while(True):
        try:
            inp=int(input(" enter 1 for displaying the books\n"
                      " enter 2 for adding the book\n"
                      " enter 3 fo lending the book \n"
                      " enter 4 for returning the book\n"
                      " enter 5 to show the rented books"))
            if inp == 1:
                Bhatkal.Displaybooks()
            elif inp == 2:
                boo=input("enter the book name : ")
                Bhatkal.Addbook(boo)
            elif inp ==3:
                username=input("enter the name of the user")
                bookname=input("enter the book name : ")
                Bhatkal.Lendbook(bookname,username)
            elif inp == 4:
                returnbook=input("enter the book name : ")
                Bhatkal.Returnbook(returnbook)
            elif inp ==5:
                print(Bhatkal.lendbook)
            else:
                print("Invalid input")
                continue
            while(True):
                c=input("press c for continue or q for quit")
                if c == "q":
                    exit()
                elif c == "c":
                    break
                else:
                    print("you have entered incorrect input ")
                    continue
        except Exception as e :
            print(e, 'error')
            print("watch the error and correct it ")


