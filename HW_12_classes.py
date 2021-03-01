from math import sqrt
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Figure:
    pass

class Point(Figure):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle(Figure):
    def __init__(self, x, y, rad):
        self.x = x
        self.y = y
        self.rad = rad

    def square_circle(self):
        circle_square = 3.14 * self.rad**2
        return f' circle square: {round(circle_square)}'

    def length_circle(self):
        circle_length = 3.14 * self.rad**2
        return f' circle square: {round(circle_length)}'

class Triangle(Figure):

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def sides(self):
        a = round(sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2))
        b = round(sqrt((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2))
        c = round(sqrt((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2))
        return a, b, c

    def perimeter(self):
        a, b, c = self.sides()
        perimeter = a + b + c
        return  perimeter


    def square(self):
        perim = self.perimeter() / 2
        a, b, c = self.sides()
        sq = round(sqrt(perim * (perim - a) * (perim - b) * (perim - c)))
        return f' triangle square: {sq}'


class Square(Figure):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def perimeter(self):
        perimeter =round(sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2) * 4)
        return f' perimeter square: {perimeter}'
    def square(self):
        square = round(sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)**2)
        return f' square square: {square}'