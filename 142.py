"""
Define a user defined type named Shape. Derive a type Square from Shape. The Square
takes length as an argument. Add a function area() in both the types. Shape's area is 0 by
default.Write the implementation for the following interface.
aSquare= Square(3)
print (aSquare.area())
aShape=Shape()
print(aShape.area())
"""
class Shape:
  def area(self):
    return 0
class Square(Shape):
  def __init__(self, l):
    Shape.__init__(self)
    self.length =l
  def area(self):
    return self.length*self.length

aSquare= Square(3)
print (aSquare.area())
