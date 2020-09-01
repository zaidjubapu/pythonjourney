import random
def rohan_table(no):
    '''to generate the table of given numbers'''
    a=random.randint(1,10)
    table=[]
    if no!=5:
        for i in range(1,11):
            if i == a:
                table.append(no*i+2)
            else:
                table.append(i*no)
    else:
        for i in range(1,11):
            table.append(i*no)
    return table
def is_correct(no,tables):
    '''to check whether the return table is correct or not '''
    list2=[]
    for i in range(1, 11):
        list2.append(i * no)
    if list2 == tables:
        return "he is not fraud"
    else:
        a=0
        for i in tables:
            if i%no != 0:
                return f"he has done fraude at {a} index "
            a+=1



if __name__ == '__main__':
    no=int(input("enter the no you want to get the multiple: "))
    a=rohan_table(no)
    b=is_correct(no,a)
    print(a)
    print(b)