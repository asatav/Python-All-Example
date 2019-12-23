class P:
    def property(self):
        print("Gold+Land+Cash+Power")
    def marry(self):
        print("ASHISH")
class C(P):
    def marry(self):
        super().marry()
        print("AJIT")
c=C()
c.property()
c.marry()