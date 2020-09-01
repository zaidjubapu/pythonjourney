class schools:
    def __init__(self,cls):
        self.cls=cls
        self.classes=cls
        self.atten=cls
        # self.cls[0]=["zaid","zai"]
        # self.cls[1]=["zuha","sara"]
        # self.cls[2]=["ahmed","zaid"]
        # self.cls[3]=['bibi',"abdul"]
        # self.cls[4]=["noor","jubapu"]
    def studentnames(self):
        b=0
        for i in self.classes:
            self.cls[b]=input(f"enter {i} class student names with space : ").split()
            b=b+1
    def attendance(self):
        while True:
            d=input("enter the class name : ")
            e=0
            for i in self.classes:
                if i==d:
                    print(f"the students are {self.cls[e]}")
                    aa=self.cls[e]
                    bb=len(aa)
                    tt=0
                    while bb>0:
                        dd=int(input(f"{aa[tt]} is present or not if yes press 1 or press 0"))
                        b=self.cls.copy()
                        b[tt]=[]
                        ee=b[tt].append(dd)
                        bb=bb+1
                        tt=tt+1
                        qq={}
                        h=qq.update({aa[tt]:b[tt]})
                    print(bb[0])
                    print(h)
                # else:
                #     print("invalid input")
                e=e+1
                # break
        # while True:
            a=input("press c for continue q for quit")
            if a=="c":
                continue
            elif aa=='q':
                break
            else:
                print("invalid input")


if __name__ == '__main__':
    '''college=input("enter the school names with space : ")
    colleges=college.split()
    lc=len(colleges)
    a=0
    while (a<lc) :'''
    aitm=schools(["a","b","c","d","e"])
    while(True):
        ll = int(input("enter the 1 for adding class stdents 2 for taking attendance 3 for exit"))
        if ll==1:
            aitm.studentnames()
        elif ll==2:
            aitm.attendance()
        elif ll==3:
            exit()
        else:
            print("invalid input")


