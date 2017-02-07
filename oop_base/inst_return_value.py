from oop_base import point
p = point.Point(3, 4)
q = point.Point(5, 12)

mid = p.halway(q)
print(mid)
print(mid.get_x())
print(mid.get_y())