class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self,other):
        return self.marks>other.marks
    def __le__(self,other):
        return self.marks<=other.marks
print("10>20=",10>20)
s1=Student("ASHISH",100)
s2=Student("AJIT",200)
print("s1>s2=",s1>s2)
print("s1<s2=",s1<s2)
print("s1>=s2=",s1>=s2)
print("s1<=s2=",s1<=s2)
