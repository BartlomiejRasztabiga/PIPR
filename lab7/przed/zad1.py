from math import sqrt


class Planet:

    def __init__(self, x, y, z, name=""):
        self.name = name
        self.number_of_moons = 0
        self.x = x
        self.y = y
        self.z = z

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def number_of_moons(self):
        return self.__number_of_moons

    @number_of_moons.setter
    def number_of_moons(self, number_of_moons):
        self.__number_of_moons = number_of_moons

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, z):
        self.__z = z

    def __str__(self):
        return f"{self.name} at {self.x},{self.y},{self.z} with {self.number_of_moons} moons"


def distance(planet1: Planet, planet2: Planet) -> float:
    return sqrt((planet1.x - planet2.x) ** 2 + (planet1.y - planet2.y) ** 2 + (planet1.z - planet2.z) ** 2)
