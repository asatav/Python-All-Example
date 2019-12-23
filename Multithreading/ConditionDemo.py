from threading import *
def consumer(c):
    c.acquire()
    print("Comsumer waiting for updation ")
    c.wait()
    print("Consumer got notification and consumong the item")
    c.release()
def producer(c):
    c.acquire()
    print("Producer producing item ")
    print("Producer giving notification ")
    c.notify()
    c.release()
c=Condition()
t1=Thread(target=consumer,args=(c,))   
t2=Thread(target=producer,args=(c,))   
t1.start()
t2.start() 