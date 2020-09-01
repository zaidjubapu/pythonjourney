import time
from functools import lru_cache

@lru_cache(maxsize=10) # from my view: it will not run the function if the same arguments is passed  in the function
def somework(n):
    # time.sleep(n)
    print(n)
    # return n
if __name__=='__main__':
    print("hello world")
    somework(3)
    input("type")
    somework(3)
    print("t")
    somework(4)
    input("tye")
    somework(4)
    somework(5)
    print("zaid")
    somework(5)
    somework(5)
    print("thankyou")

