from threading import *
import time
from Demo5 import doubles, square
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print("Double:",2*n)
def square(numbers):
    for n in numbers:
        time.sleep(1)
        print("Square:",n*n)
numbers=[1,2,3,4,5,6,7,8,9]
begintime=time.time()
t1=Thread(target=doubles,args=(numbers))
t2=Thread(target=square,args=(numbers))
t1.start()
t2.start()
t1.join()
t2.join()
print("The totle time taken:",time.time()-begintime)