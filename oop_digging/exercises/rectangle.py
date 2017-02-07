from oop_digging.exercises.point import Point
import math


class Rectangle:
    """Rectangle class using Point, width and height"""

    def __init__(self, init_point, init_w, init_y):
        self.location = init_point
        self.width = init_w
        self.height = init_y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def area(self):
        return self.width * self.height

    def perimer(self):
        return self.width * 2 + self.height * 2

    def transponse(self):
        old_width = self.width
        self.width = self.height
        self.height = old_width

    def diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def contains(self, point):
        if self.check_location(self.location.x, self.width, point.x) and self.check_location(self.location.y, self.height, point.y):
            return True
        return False

    @classmethod
    def check_location(cls, point1, point2, point):
        if point1 <= point and point2 > point:
            return True
        return False
loc = Point(0, 0)
r = Rectangle(loc, 10, 5)
print(r.diagonal())
print(r.contains(Point(1, 4)))
print(r.contains(Point(3, 7)))
print(r.area())
print(r)
