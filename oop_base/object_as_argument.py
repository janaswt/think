import math
from oop_base import point

def distance(point1, point2):
    x_diff = point2.get_x() - point1.get_x()
    y_diff = point2.get_y() - point1.get_y()
    
    dist = math.sqrt(x_diff ** 2 + y_diff ** 2)
    return dist
p = point.Point(4, 3)
q = point.Point(0, 0)
ss = distance(p, q)
print(ss)
