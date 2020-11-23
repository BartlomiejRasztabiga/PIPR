import pytest
from zad1 import Planet, distance


def test_distance():
    planet1 = Planet(1, 3, 5, "XYZ")
    planet2 = Planet(-3, 43, 3, "ABC")

    assert distance(planet1, planet2) == pytest.approx(40.2492)


def test_distance2():
    planet1 = Planet(1, 1, 1, "XYZ")
    planet2 = Planet(1, 1, 1, "ABC")

    assert distance(planet1, planet2) == pytest.approx(0)
