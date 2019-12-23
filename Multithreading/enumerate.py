from threading import *
import time
def display():
    print(current_thread().getName(),"....started")
    time.sleep(3)
    print(current_thread().getName(),"....ended")
print("The number of active thread",active_count())
t1=Thread(target=display,name="schildthread1")
t2=Thread(target=display,name="schildthread2")
t3=Thread(target=display,name="schildthread3")
t1.start()
t2.start()
t3.start()
i=enumerate()
for t in i:
    print("Thread name:",t.name)
time.sleep(5)
i=enumerate()
for t in i:
    print("Thread name:",t.name)
