class Student:
    '''This is student class with  required data'''
def __init__(self,x,y,z):
    self.name=x
    self.rollno=y 
    self.marks=z 
def display(self):
    print("Student name:{}\nRollno:{}\nMarks:{}".format(self.name,self.rollno,self.marks))

s1=Student("ASHISH",101,100)
s1.display()
s2=Student("Ajit",102,99)
s2.display()