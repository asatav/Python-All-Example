from threading import *
import time
def display():
    for i in range(10):
        print("ASHISH THREAD")
        time.sleep(2)
t=Thread(target=display)
t.start()
t.join(5)
for i in range(10):
    print("AJIT THREAD")
