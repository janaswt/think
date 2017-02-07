import math
class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    def __init__(self, init_x=0, init_y=0):
        self.x = init_x
        self.y = init_y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    def halway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)
    def distance_from_point(self, other_p):
        dx = (other_p.get_x() - self.x)
        dy = (other_p.get_y() - self.y)
        return math.sqrt(dy ** 2 + dx ** 2)
    def reflex_x(self):
        return Point(self.x, -self.y)
    def slope_from_origin(self):
        if self.x != 0:
            return self.y / self.x
        return None
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        
    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

if __name__ == "__main__":
    p = Point(7, 6)
    print(p.get_x())
    print(p.get_y())
    print(p.distance_from_origin())
    q = Point()

    print("Nothing seems to have happened with the points")
    
    print(p)
    print(q)
    
    print(p is q)
    print(p == q)
    p = Point(3, 3)
    q = Point(6, 7)
    print(p.distance_from_point(q))
    print(p.reflex_x())
    print(q.slope_from_origin())