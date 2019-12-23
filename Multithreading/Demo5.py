from threading import *
import time
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
doubles(numbers)
square(numbers)
print("The totle time taken:",time.time()-begintime)