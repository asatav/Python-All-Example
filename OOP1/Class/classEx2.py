class Student:
    
def __init__(self,name,rollno,marks):
   self.name=name
   self.rollno=rollno
   self.marks=marks
   
def talk(self):
    print("Hello i am",self.name)
    print("My age is ",self.rollno)
    print("My marks are",self.marks)
s=Student("Ashish",1,100)
s.talk()
