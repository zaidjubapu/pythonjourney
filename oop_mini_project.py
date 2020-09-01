Booksavail=["C++","Java","python","Swift","Mathematics","Science"]
LendBook={}
def displayBooks():
    '''to display books available in library'''

    print("The books available in library are: ",end=" ")
    for i in Booksavail:
        print(i,end=", ")
    print("\n")
print(displayBooks.__doc__)


def AddBook():
    '''to add the books in library'''
    b=input("enter the book you want to add")
    Booksavail.append(b)
    print("The book is successfully added")
def lendBook():
    '''to take the book in rent'''
    try:
        n=input("enter your name : ")
        b=input("enter the book name : ")
        if b in Booksavail:
            print("you can take the book")
            LendBook.update({b:n})
            Booksavail.remove(b)
        else:
            print("books is not availble")
            print("it has been taken by ",LendBook[b])
    except Exception as e:
        print("this book is not in their list")

def returnbook():
    try:
        b=input("enter the book which you want to return : ")
        Booksavail.append(b)
        LendBook.pop(b)
        print("you have successfully return a book")
    except Exception as e:
        print("this book is not rented")
        print(e,"error")
while(True):
    print('Welcome to library')
    inp=int(input("enter the no as given below:"
                  "1 for dispay books"
                  "2 for add book"
                  "3 for Lend book"
                  "4 for return book "))
    if inp == 1:
        displayBooks()
    elif inp == 2:
        AddBook()
    elif inp == 3:
        lendBook()
    elif inp == 4:
        returnbook()
    else:
        print("INVALID INPUT")
    # re=input("press q for quit and c for continue")
    af=""
    while(af!="q" or af !="c") :
        re = input("press q for quit and c for continue")
        if re=="q":
            exit()
        elif re=="c":
            print('thankyou you can use one more time')
            break
        else:
            print("invalid input")
            print("enter again")
print(lendBook.__docstring__())






