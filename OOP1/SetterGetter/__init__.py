class Student:
  def setName(self,name):
      self.name=name
  def getName(self):
      return self.name
  def setMarks(self,marks):
      self.marks=marks
  def getMarks(self):
      return self.marks
n=int(input('Enter number of student'))
for i in range(n):
    s=Student()
    name=input('Enter Name:-')
    s.setName(name)
    marks=int(input('Enter your marks'))
    s.setMarks(marks)
    print('HI',s.getName())
    print('Your Marks are',s.getMarks())
    print()
    
   