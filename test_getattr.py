import math
import operator


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y}"

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y -y)


p = Point(2, 3)
d = getattr(p, 'distance')(0,0)
print(d)
print(operator.methodcaller('distance', 0, 0)(p))
