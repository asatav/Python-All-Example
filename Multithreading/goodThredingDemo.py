from threading import *
import time
l=Lock()
def wish(name):
    l.acquire()
    try:
        for i in range(10):
            print("Good evening",end=" ")
            time.sleep(2)
            print(name)
    finally:
        l.release()
t1=Thread(target=wish,args=("ASHISH",))
t2=Thread(target=wish,args=("AJIT",))
t3=Thread(target=wish,args=("ROHINI",))
t1.start()
t2.start()
t3.start()
            