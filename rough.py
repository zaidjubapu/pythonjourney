# # # a="hello"
# # # b="python"
# # # print(a,b,"fish",sep="zain",end="!")
# # # print(a,b,"zain",end="!")
# # a=["ima zaid","iam zuha"]
# # z=a.sort()
# # print(a)
# # import pyaudio
# b=open("zaid.txt",'r')
# for a in b:
#     a=a.rstrip()
#     print(a)
# import pyaudio1
#to tell you in wich your you will become 100 year old
class age:
    cy=2020
    # def __init__(self,a):
    #     self.ag=a
    #     self.ye=a
    def year(self):
        print(f"you will become 100 year old at the year{a+100}")
    def ages(self):
        print(f"you will become 100 year old at the year {age.cy-a + 100}")



if __name__ == '__main__':
    print("to tell you in which year you will become 100 year old")
    while True:
        try:
            classage=age()
            a=int(input("please enter year of birth or your current age : "))
            if a>200:
                classage.year()
            else:
                classage.ages()

        except Exception as e:
            print(f"the error is {e}")
        b=input("press s to continue or n to exit")
        if b == "s":
            continue
        else:
            break


