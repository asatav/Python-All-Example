from threading import *
def test():
    print("Child thread")
t=Thread(target=test)
t.start()
print("Main thread identification Number:",current_thread().ident)
print("child thread identification Number:",t.ident)
