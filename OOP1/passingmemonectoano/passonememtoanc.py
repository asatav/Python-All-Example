class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print('Employee no',self.eno)
        print('Employee name',self.ename)
        print('Employee sal',self.esal)
class Test:
    def modify(emp):
        emp.esal=emp.esal+10000
        emp.display()
e=Employee(100,'ASHISH',470000)
Test.modify(e)
        