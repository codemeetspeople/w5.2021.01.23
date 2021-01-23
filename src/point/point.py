from pympler.asizeof import asizeof


class Point:
    # __slots__ = ['x', 'y']

    def __init__(self, x=0.0, y=0.0):
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = float(value)

    @y.setter
    def y(self, value):
        self._y = float(value)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError()
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def get_size(self):
        return asizeof(self)
