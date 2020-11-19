import pytest
from zad3 import (get_lab_points,
                  get_sum_of_lab,
                  get_student_avg_lab_percentage,
                  get_single_student_summary,
                  get_all_students_summary,
                  get_all_students_avg_lab_score)


def test_get_lab_points_regular():
    assert get_lab_points([5, 10, 15]) == [5, 10, 15]


def test_get_lab_points_empty():
    assert get_lab_points([]) == []


def test_get_lab_points_wrong_value():
    assert get_lab_points([5, '1o', 15]) is None


def test_get_lab_point_not_array():
    assert get_lab_points(55) is None


def test_get_lab_point_none():
    assert get_lab_points(None) is None
