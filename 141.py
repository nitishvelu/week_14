"""Create a Student class and initialize it with name and roll number. Create methods to :
1. Display - It should display all informations of the student.
2. setAge - It should assign age to student
3. setMarks - It should assign marks to the student.
Write a test script to test the class with its instance(s).
Solution:
"""
class Student():
  def __init__(self,name,roll):
    self.name = name
    self.roll= roll
  def display(self):
    print (self.name)
    print (self.roll)
def setAge(self,age):
  self.age=age
def setMarks(self,marks):
  self.marks = marks
a=Student("hello",123)
a.display()
