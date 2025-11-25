from Graphics.RectFunctions import RectArea,RectPerimeter
from Graphics.CirFunctions import CirPerimeter,CirArea
from Graphics.DGraphics.SphereFunctions import SpArea,SpPerimeter
from Graphics.DGraphics.CuboidFunctions import CubPerimeter,CubArea

# Rectangle
l=int(input("Enter length: "))
b=int(input("Enter breadth: "))
print("Rectangle Area =",RectArea(l,b))
print("Rectangle Perimeter =",RectPerimeter(l,b))

# Circle
r=int(input("Enter radius of Circle: "))
print("Circle Area =",CirArea(r))
print("Circle Perimeter =",CirPerimeter(r))

# Sphere
r=int(input("Enter radius of Sphere: "))
print("Sphere Area =",SpArea(r))
print("Sphere Volume =",SpPerimeter(r))

# Cuboid
l=int(input("Enter cuboid length: "))
b=int(input("Enter cuboid breadth: "))
h=int(input("Enter cuboid height: "))
print("Cuboid Area =",CubArea(l,b,h))
print("Cuboid Perimeter =",CubPerimeter(l,b,h))
