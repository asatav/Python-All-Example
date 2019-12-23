class P:
    def m1(self):
        print("parent method")
class C(P):
    def m2(self):
         print("child method")
class CC(C):
    def m3(self):
         print("sub child method")
c=CC()
c.m1()
c.m2()
c.m3()