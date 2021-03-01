"""
Create a Point class describing the point (attributes: x, y).
Create class Figure. Create three child classes Circle
(attributes: center coordinates (Point type), radius length; methods:
finding the perimeter and area of a circle), Triangle
(attributes: three points, methods: finding the area and perimeter),
Square (attributes: two points, methods : finding area and perimeter).
If necessary, create all the necessary methods not described in the assignment.
Create a list of figures and in a loop calculate and display the areas of all figures on the screen

"""
from classes import Circle,Triangle, Square

circle = Circle(3, 4, 20)
triangle = Triangle(0,0, 5, 5, 10, 0)
square = Square(0, 0, 15, 25)
print(circle.square_circle())
print(f' triangle square: {triangle.perimeter()}')
print(triangle.square())
print(square.perimeter())
print(square.square())