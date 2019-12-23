class P:
    a=10
    def __init__(self):
        self.b=10
    def m1(self):
        print("parent instance method")
    @classmethod
    def m2(cls):
        print("parent class method")
    @staticmethod
    def m3():
        print('parent static method')
class C(P):
    pass
c=C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()