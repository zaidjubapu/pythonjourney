class age:
    current_year=2020
    def __init__(self,year,length):
        self.year=year
        self.length=length
    def yearss(self):
        yer=self.year+100
        print(f"you will become 100 years old at the year {yer}")
    def ages(self):
        aeg=age.current_year-self.year+100
        print(f"you will become 100 years old at the year{aeg}")
if __name__ == '__main__':
    while True:
        try:
            print("to tell  the year when you will become 100 year old")
            a=input("enter the age or year of birth : ")
            l=len(a)
            a=int(a)
            person=age(a,l)
            if a >age.current_year:
                print("you have entered bigger age")
            elif a<0:
                print("you have entered lesser age")
            elif l==4:
                person.yearss()
            elif l>0:
                person.ages()
            else:
                print("incorrect input")


        except Exception as e:
            print(f"the error is {e} .has occured ")
        finally:
            a=input('for continue press s else n:')
            if a=="n":
                break

print("thankyou for using")

