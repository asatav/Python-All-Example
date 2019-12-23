class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatndrink(self):
        print("Eat Biryani and Drink Beer")
class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name, age)
        self.eno=eno
        self.esal=esal
    def work(self):
        print("Coding python is very easy like drinking chillled beer")
    def empinfo(self):
        print("Employee Name:",self.name)
        print("Employee Age:",self.age)
        print("Employee NUmber:",self.eno)
        print("Employee Salary:",self.esal)
e=Employee("ASHISH",48,100,345678)
e.eatndrink()
e.work()
e.empinfo()