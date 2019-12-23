class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getinfo(self):
        print("Car Name:{},Model:{},Color:{}".format(self.name,self.model,self.color))
        
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatndrink(self):
        print("Eat Biryani and Drink Beer")
class Employee(Person):
    def __init__(self,name,age,eno,esal,car):
        super().__init__(name, age)
        self.eno=eno
        self.esal=esal
        self.car=car
    def work(self):
        print("Coding python is very easy like drinking chillled beer")
    def empinfo(self):
        print("Employee Name:",self.name)
        print("Employee Age:",self.age)
        print("Employee NUmber:",self.eno)
        print("Employee Salary:",self.esal)
        self.car.getinfo()
c=Car("Endavour","3.4V","White")
e=Employee("ASHISH",48,100,345678,c)
e.eatndrink()
e.work()
e.empinfo()