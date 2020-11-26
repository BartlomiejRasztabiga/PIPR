class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    @property
    def top_left(self):
        return self._top_left

    @top_left.setter
    def top_left(self, top_left):
        self._top_left = top_left

    @property
    def bottom_right(self):
        return self._bottom_right

    @bottom_right.setter
    def bottom_right(self, bottom_right):
        self._bottom_right = bottom_right

    @property
    def bottom_left(self):
        a = self._get_first_side()
        return Point(self.bottom_right.x - a, self.bottom_right.y)

    @property
    def top_right(self):
        a = self._get_first_side()
        return Point(self.top_left.x + a, self.top_left.y)

    def _get_first_side(self):
        return abs(self.top_left.x - self.bottom_right.x)

    def _get_second_side(self):
        return abs(self.top_left.y - self.bottom_right.y)

    def get_area(self):
        a = self._get_first_side()
        b = self._get_second_side()
        return a * b

    def get_perimeter(self):
        a = self._get_first_side()
        b = self._get_second_side()
        return 2 * a + 2 * b
