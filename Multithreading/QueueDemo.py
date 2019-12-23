from threading import *
import time
import random
import queue
from test.test_enum import threading
def produce(q):
    while True:
        item=random.randint(1,100)
        print("Producer producing item:",item)
        q.put(item)
        print("Producer giving notification ")
        time.sleep(5)
def consume(q):
    while True:
        print("Cosumer waiting for updation ")
        print("Consumer consumed the item:",q.get())
        time.sleep(5)
q=queue.Queue()
t1=Thread(target=consume,args=(q,))   
t2=Thread(target=produce,args=(q,))   
t1.start()
t2.start()