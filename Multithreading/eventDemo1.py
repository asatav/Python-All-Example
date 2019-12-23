from threading import *
import time
def producer():
    time.sleep(5)
    print("Producer thread producing new item:")
    print("Producer thread giving notification by setting event")
    event.set()
def consumer():
    print("Consumer thread is waiting for updation ")
    event.wait()
    print("Cosumer thread got notification and consuming items ")
event=Event()
t1=Thread(target=producer)
t2=Thread(target=consumer)
t1.start()
t2.start()