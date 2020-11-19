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
    with pytest.raises(ValueError):
        get_lab_points([5, '1o', 15])


def test_get_lab_point_not_array():
    with pytest.raises(ValueError):
        get_lab_points(55)


def test_get_lab_point_none():
    with pytest.raises(ValueError):
        get_lab_points(None)


def test_get_sum_of_lab_regular1():
    assert get_sum_of_lab(("Adam Abacki", [5, 10, 15])) == 30


def test_get_sum_of_lab_regular2():
    assert get_sum_of_lab(("Cecylia Cabacka", [1, 2, 3])) == 6


def test_get_sum_of_lab_wrong_value():
    assert get_sum_of_lab(("Adam Abacki", [5, '1o', 15])) == None


def test_get_sum_of_lab_not_array():
    assert get_sum_of_lab(("Cecylia Cabacka", 55)) == None


def test_get_student_avg_lab_percentage_regular1():
    assert get_student_avg_lab_percentage(
        ("Adam Abacki", [5, 10, 15]), [10, 20, 30]) == 50


def test_get_student_avg_lab_percentage_regular2():
    assert get_student_avg_lab_percentage(
        ("Cecylia Cabacka", [1, 2, 3]), [10, 20, 30]) == 10


def test_get_student_avg_lab_percentage_wrong_value():
    assert get_student_avg_lab_percentage(
        ("Adam Abacki", [5, '1o', 15]), [10, 20, 30]) == None


def test_get_student_avg_lab_percentage_not_array():
    assert get_student_avg_lab_percentage(
        ("Adam Abacki", 55), [10, 20, 30]) == None


def test_get_single_student_summary_regular1():
    assert get_single_student_summary(
        ("Adam Abacki", [5, 10, 15]), [10, 20, 30]) == ("Adam Abacki", 30, 50)


def test_get_single_student_summary_regular2():
    assert get_single_student_summary(
        ("Cecylia Cabacka", [1, 2, 3]), [10, 20, 30]) == ("Cecylia Cabacka", 6, 10)


def test_get_single_student_summary_wrong_value():
    assert get_single_student_summary(
        ("Adam Abacki", [5, '1o', 15]), [10, 20, 30]) == ("Adam Abacki", None, None)


def test_get_single_student_summary_not_array():
    assert get_single_student_summary(
        ("Cecylia Cabacka", 55), [10, 20, 30]) == ("Cecylia Cabacka", None, None)


def test_get_all_students_summary_regular():
    assert get_all_students_summary(
        [("Adam Abacki", [5, 10, 15]), ("Basia Babacka", [10, 20, 30]), ("Cecylia Cabacka", [1, 2, 3])], [10, 20, 30]) == [("Adam Abacki", 30, 50), ("Basia Babacka", 60, 100), ("Cecylia Cabacka", 6, 10)]


def test_get_all_students_summary_wrong_values():
    assert get_all_students_summary(
        [("Adam Abacki", [5, '1o', 15]), ("Basia Babacka", [10, 20, 30]), ("Cecylia Cabacka", 55)], [10, 20, 30]) == [("Adam Abacki", None, None), ("Basia Babacka", 60, 100), ("Cecylia Cabacka", None, None)]


def test_get_all_students_avg_lab_score_regular():
    assert get_all_students_summary(
        [("Adam Abacki", [5, 10, 15]), ("Basia Babacka", [10, 20, 30]), ("Cecylia Cabacka", [1, 2, 3])], [10, 20, 30]) == 32


def test_get_all_students_avg_lab_score_wrong_values():
    assert get_all_students_summary(
        [("Adam Abacki", [5, '1o', 15]), ("Basia Babacka", [10, 20, 30]), ("Cecylia Cabacka", 55)], [10, 20, 30]) == 100
