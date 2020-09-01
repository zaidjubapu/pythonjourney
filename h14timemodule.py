'''
time module:
used for to know howm much time the comp take to run the prg

import time
initial=time.time()
k=0
while(k<100):
    print('zaid')
    k+=1
print("while loop ran in: ",time.time()-initial,"seconds")
intial2=time.time()
for i in range(100):
    print('zaid')
print("for loop  ran in: ",  time.time()-intial2, 'sec')

# another function;

import time
localtime=time.asctime(time.localtime(time.time()))
print(localtime)
localtim=time.localtime(time.time())
print(localtim)
print(time.asctime(localtim))

another function:
time.sleep
'''
import time
k=0
while(k<10):
    print('zaid')
    k+=1
    time.sleep(2)# it will move forward after two sec