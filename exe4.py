'''the next palindrome
input:you have to take the input from the user .you have to find the next paalindrome corresponding to that number.
you have to take no test cases ..and give the input
ex:
input:
3
431
635
2134
output:
your next palindrome no is 434
your next palindrome no is 636
your next palindrome no is 2222
'''
#taking the inputs
if __name__ == '__main__':
    a=int(input("enter the no of cases you want to test : "))
    mylist=[]
    for i in range(a):
        a=input(f"enter the {i+1} case no ")
        mylist.append(a)
    # mylist=[431,535,212]
    z=len(mylist)
    list1=mylist.copy()
    for i in range(z):
        a=str(list1[i])
        a=a[::-1]
        # print(a)
        if a == str(list1[i]):
            print(f"{list1[i]} is an palindrome no")
        elif a != str(list1[i]):
            print(f"{list1[i]} is not an palindrom no")
            a = int(list1[i])
            while True:
                a=a+1
                c = str(a)
                b = c[::-1]
                if str(a) == b:
                    print(f"your next palindrome no is {b}")
                    break


