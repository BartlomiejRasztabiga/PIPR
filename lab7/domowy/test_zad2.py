import pytest
from zad2 import Route, RoutePoint, Stop, Time, InvalidTimeException


def __prepare_simple_route_points():
    return [
        RoutePoint(Stop('stop 1', False, Time(0, 0)), Time(0, 0)),
        RoutePoint(Stop('stop 2', False, Time(0, 0)), Time(0, 1)),
        RoutePoint(Stop('stop 3', False, Time(0, 0)), Time(0, 2))
    ]


def __prepare_complex_route_points():
    return [
        RoutePoint(Stop('stop 1', False, Time(0, 1)), Time(0, 0)),
        RoutePoint(Stop('stop 2', False, Time(0, 1)), Time(0, 3)),
        RoutePoint(Stop('stop 3', True, Time(0, 5)), Time(0, 4)),
        RoutePoint(Stop('stop 4', True, Time(0, 1)), Time(0, 7)),
        RoutePoint(Stop('stop 5', False, Time(0, 1)), Time(0, 2))
    ]


def test_time_create_wrong_value_hours1():
    with pytest.raises(InvalidTimeException):
        Time(25, 0)


def test_time_create_wrong_value_hours2():
    with pytest.raises(InvalidTimeException):
        Time(-25, 0)


def test_time_create_wrong_value_minutes_1():
    with pytest.raises(InvalidTimeException):
        Time(0, 65)


def test_time_create_wrong_value_minutes_2():
    with pytest.raises(InvalidTimeException):
        Time(0, -65)


def test_time_add_simple():
    time1 = Time(15, 30)
    time2 = Time(0, 15)
    assert time1 + time2 == Time(15, 45)


def test_time_add_oclock():
    time1 = Time(15, 30)
    time2 = Time(0, 30)
    assert time1 + time2 == Time(16, 00)


def test_time_add_with_carry():
    time1 = Time(15, 30)
    time2 = Time(0, 46)
    assert time1 + time2 == Time(16, 16)


def test_get_route_point_description_without_change():
    route_point = RoutePoint(Stop('stop 1', False, Time(0, 1)), Time(0, 5))
    route_point_description = route_point.get_route_point_description(Time(13, 50))
    assert route_point_description == "arrival: 13:50  departure: 13:51 (stop 1) - CHANGE_NOT_POSSIBLE"


def test_get_route_point_description_with_change():
    route_point = RoutePoint(Stop('stop 1', True, Time(0, 1)), Time(0, 5))
    route_point_description = route_point.get_route_point_description(Time(13, 50))
    assert route_point_description == "arrival: 13:50  departure: 13:51 (stop 1) - CHANGE_POSSIBLE"


def test_calculate_route_duration_without_wait_times():
    route_points = __prepare_simple_route_points()

    route = Route('A', route_points)
    route_duration = route._calculate_route_duration()
    assert route_duration == Time(0, 3)


def test_calculate_route_duration_with_wait_times():
    route_points = __prepare_complex_route_points()

    route = Route('B', route_points)
    route_duration = route._calculate_route_duration()
    assert route_duration == Time(0, 25)


def test_calculate_route_end_time():
    route_points = __prepare_simple_route_points()

    route = Route('A', route_points)
    route_end_time = route._calculate_route_end_time(Time(13, 50))
    assert route_end_time == Time(13, 53)


def test_generate_timetable_simple_without_wait_times_without_changes():
    route_points = __prepare_simple_route_points()

    route = Route('A', route_points)
    timetable = route.generate_timetable(Time(1, 5))
    assert timetable == [
        "Route A with 3 stops",
        "1:05 -> 1:08",
        "arrival: 1:05  departure: 1:05 (stop 1) - CHANGE_NOT_POSSIBLE",
        "arrival: 1:06  departure: 1:06 (stop 2) - CHANGE_NOT_POSSIBLE",
        "arrival: 1:08  departure: 1:08 (stop 3) - CHANGE_NOT_POSSIBLE"
    ]


def test_generate_timetable_complex():
    route_points = __prepare_complex_route_points()

    route = Route('B', route_points)
    timetable = route.generate_timetable(Time(1, 5))
    assert timetable == [
        "Route B with 5 stops",
        "1:05 -> 1:30",
        "arrival: 1:06  departure: 1:07 (stop 1) - CHANGE_NOT_POSSIBLE",
        "arrival: 1:10  departure: 1:11 (stop 2) - CHANGE_NOT_POSSIBLE",
        "arrival: 1:19  departure: 1:24 (stop 3) - CHANGE_POSSIBLE",
        "arrival: 1:27  departure: 1:28 (stop 4) - CHANGE_POSSIBLE",
        "arrival: 1:30  departure: 1:31 (stop 5) - CHANGE_NOT_POSSIBLE"
    ]
