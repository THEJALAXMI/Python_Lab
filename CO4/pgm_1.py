class Rect:
    def __init__(self, length, breadth):
      self.l = length
      self.b = breadth
    def area(self):
       return self.l * self.b
    def perimeter(self):
       return 2*(self.l+self.b)
x1 = int(input("Enter length of 1st rectangle: "))
y1 = int(input("Enter breadth of 1st rectangle: "))
r1 = Rect(x1, y1)
print("Area of rectangle 1:", r1.area())
print("Perimeter of rectangle 1:", r1.perimeter())
x2 = int(input("\nEnter length of 2nd rectangle: "))
y2 = int(input("Enter breadth of 2nd rectangle: "))
r2 = Rect(x2, y2)
print("Area of rectangle 2:", r2.area())
print("Perimeter of rectangle 2:", r2.perimeter())
if r1.area() == r2.area():
    print("\nAreas of both rectangles are equal.")
else:
    print("\nAreas of both rectangles are not equal.")
