sentences=["python is  python very good laguage","python python is python is cool","python is awesome","javascript is good"]
import time
# join=sentences[0].split()
# print(join)
inp=[x for x in (input("enter the word you want to search").split())]
searchmatch=[]
# dict1={}
c=time.time()
for search in inp:
    a = 0
    for i in sentences:
        a = 0
        d=i.split()
        for j in d:
            if j == search:
                a+=1
        searchmatch.append(a)
print(searchmatch)
f=[]
b=time.time()-c
# print(f'{e} result found in {b} second')
# print(searchmatch[::-1])
# print(dict1)
k=[]
for i in range(len(searchmatch)/2):
    s=searchmatch[i+4]
    k.append(s)
l=sorted((zip(k,sentences)),reverse=True)
print(l)

for i,v in l:
    if i>=1:
        f.append(v)
e=len(f)
print(f'{e} result found in {b} second')
for i in f:
    print(i)



