import pytest
from zad3 import (get_lab_points,
                  get_sum_of_lab,
                  get_student_avg_lab_percentage,
                  get_single_student_summary,
                  get_all_students_summary,
                  get_all_students_avg_lab_score)

max_lab_points = [10, 20, 30]


def test_get_lab_points_regular():
    assert get_lab_points([5, 10, 15], max_lab_points) == [5, 10, 15]


def test_get_lab_points_empty():
    assert get_lab_points([], max_lab_points) == []


def test_get_lab_points_wrong_value():
    with pytest.raises(ValueError):
        get_lab_points([5, '1o', 15], max_lab_points)


def test_get_lab_point_not_array():
    with pytest.raises(ValueError):
        get_lab_points(55, max_lab_points)


def test_get_lab_point_none():
    with pytest.raises(ValueError):
        get_lab_points(None, max_lab_points)


def test_get_sum_of_lab_regular1():
    assert get_sum_of_lab(("Adam Abacki", [5, 10, 15]), max_lab_points) == 30


def test_get_sum_of_lab_regular2():
    assert get_sum_of_lab(("Cecylia Cabacka", [1, 2, 3]), max_lab_points) == 6


def test_get_sum_of_lab_wrong_value():
    assert get_sum_of_lab(
        ("Adam Abacki", [5, '1o', 15]), max_lab_points) is None


def test_get_sum_of_lab_not_array():
    assert get_sum_of_lab(("Cecylia Cabacka", 55), max_lab_points) is None


def test_get_student_avg_lab_percentage_regular1():
    assert get_student_avg_lab_percentage(
        ("Adam Abacki", [5, 10, 15]), [10, 20, 30]) == 50


def test_get_student_avg_lab_percentage_regular2():
    assert get_student_avg_lab_percentage(
        ("Cecylia Cabacka", [1, 2, 3]), [10, 20, 30]) == 10


def test_get_student_avg_lab_percentage_too_short():
    assert get_student_avg_lab_percentage(
        ("Cecylia Cabacka", [1, 2]), [10, 20, 30]) == 5


def test_get_student_avg_lab_percentage_wrong_value():
    assert get_student_avg_lab_percentage(
        ("Adam Abacki", [5, '1o', 15]), [10, 20, 30]) is None


def test_get_student_avg_lab_percentage_not_array():
    assert get_student_avg_lab_percentage(
        ("Adam Abacki", 55), [10, 20, 30]) is None


def test_get_single_student_summary_regular1():
    result = get_single_student_summary(
        ("Adam Abacki", [5, 10, 15]), [10, 20, 30])
    assert result == ("Adam Abacki", 30, 50)


def test_get_single_student_summary_regular2():
    result = get_single_student_summary(
        ("Cecylia Cabacka", [1, 2, 3]), [10, 20, 30])
    assert result == ("Cecylia Cabacka", 6, 10)


def test_get_single_student_summary_wrong_value():
    result = get_single_student_summary(
        ("Adam Abacki", [5, '1o', 15]), [10, 20, 30])
    assert result == ("Adam Abacki", None, None)


def test_get_single_student_summary_not_array():
    result = get_single_student_summary(
        ("Cecylia Cabacka", 55), [10, 20, 30])
    assert result == ("Cecylia Cabacka", None, None)


def test_get_all_students_summary_regular():
    assert get_all_students_summary([
        ("Adam Abacki", [5, 10, 15]),
        ("Basia Babacka", [10, 20, 30]),
        ("Cecylia Cabacka", [1, 2, 3])
    ], [10, 20, 30]) == [
        ("Adam Abacki", 30, 50),
        ("Basia Babacka", 60, 100),
        ("Cecylia Cabacka", 6, 10)
    ]


def test_get_all_students_summary_wrong_values():
    assert get_all_students_summary([
        ("Adam Abacki", [5, '1o', 15]),
        ("Basia Babacka", [10, 20, 30]),
        ("Cecylia Cabacka", 55)
    ], [10, 20, 30]) == [
        ("Adam Abacki", None, None),
        ("Basia Babacka", 60, 100),
        ("Cecylia Cabacka", None, None)
    ]


def test_get_all_students_avg_lab_score_regular():
    assert get_all_students_avg_lab_score([
        ("Adam Abacki", [5, 10, 15]),
        ("Basia Babacka", [10, 20, 30]),
        ("Cecylia Cabacka", [1, 2, 3])
    ], max_lab_points) == 32


def test_get_all_students_avg_lab_score_wrong_values():
    assert get_all_students_avg_lab_score([
        ("Adam Abacki", [5, '1o', 15]),
        ("Basia Babacka", [10, 20, 30]),
        ("Cecylia Cabacka", 55)
    ], max_lab_points) == 60
