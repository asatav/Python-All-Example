from threading import *
import time
l=Semaphore(3)
def wish(name):
    l.acquire()
    for i in range(10):
        print("Good evening",end="")
        time.sleep(2)
        print(name)
    l.release()
t1=Thread(target=wish,args=("ASHISH",))
t2=Thread(target=wish,args=("AJIT",))
t3=Thread(target=wish,args=("Rohini",))
t1.start()
t2.start()
t3.start()