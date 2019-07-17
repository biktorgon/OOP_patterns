import math


class Hole:
    def __init__(self, r):
        self.r = r

    def fit(self, obj):
        try:
            if self.r >= obj.r:
                print("It's fit")
            else:
                print("It's not fit")
        except AttributeError:
            print("This object could't calculate radius."
                "Try to use Adapter")


class Square:
    def __init__(self, x, h):
        self.x = x
        self.h = h


class SquareHoleAdapter:
    def __init__(self, sq_obj):
        self.sq_obj = sq_obj

    @property
    def r(self):
        return math.sqrt(2 * (self.sq_obj.x ** 2)) / 2


h1 = Hole(5)
h2 = Hole(2)
s1 = Square(5, 7)
s2 = Square(3, 3)
sa = SquareHoleAdapter(s2)

h1.fit(s1)

h1.fit(sa)

h2.fit(sa)
