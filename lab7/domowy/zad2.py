from dataclasses import dataclass

from typing import List


@dataclass()
class InvalidTimeException(Exception):
    message: str


@dataclass()
class Time:
    hours: int
    minutes: int

    def __post_init__(self):
        if self.hours > 24 or self.hours < 0:
            raise InvalidTimeException("Hours are in invalid range")
        elif self.minutes > 60 or self.minutes < 0:
            raise InvalidTimeException("Minutes are in invalid range")

    def __add__(self, other):
        temp = Time(self.hours, self.minutes)
        temp.hours += other.hours
        temp.minutes += other.minutes

        if temp.minutes >= 60:
            temp.hours += temp.minutes // 60
            temp.minutes -= 60
        return temp

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __str__(self):
        return f"{self.hours}:{self.minutes:02}"


@dataclass()
class Stop:
    name: str
    is_possibility_to_change: bool
    wait_time: Time

    def get_stop_description(self, time_of_arrival: Time) -> str:
        time_of_departure = time_of_arrival + self.wait_time
        possibility_of_change_suffix = f"CHANGE{'_NOT' if not self.is_possibility_to_change else ''}_POSSIBLE"
        return f"arrival: {time_of_arrival}  departure: {time_of_departure} ({self.name}) - {possibility_of_change_suffix}"


@dataclass()
class RoutePoint:
    stop: Stop
    time_of_travel_since_last_stop: Time

    def get_route_point_description(self, time_of_arrival: Time) -> str:
        return self.stop.get_stop_description(time_of_arrival)

    def get_departure_delay(self):
        return self.stop.wait_time + self.time_of_travel_since_last_stop


@dataclass()
class Route:
    name: str
    route_points: List[RoutePoint]

    def _calculate_route_duration(self) -> Time:
        return sum(point.get_departure_delay() for point in self.route_points)

    def _calculate_route_end_time(self, start_time: Time) -> Time:
        route_duration = self._calculate_route_duration()
        return start_time + route_duration

    def _get_route_header_line(self) -> str:
        number_of_route_points = len(self.route_points)
        return f"Route {self.name} with {number_of_route_points} stops"

    def _get_route_start_end_times_line(self, start_time: Time):
        end_time = self._calculate_route_end_time(start_time)
        return f"{start_time} -> {end_time}"

    def _get_route_points_descriptions(self, start_time: Time):
        descriptions = []
        time_of_arrival = start_time

        for route_point in self.route_points:
            time_of_arrival += route_point.get_departure_delay()
            description = route_point.get_route_point_description(time_of_arrival)
            descriptions.append(description)

        return descriptions

    def generate_timetable(self, start_time: Time):
        timetable = [
            self._get_route_header_line(),
            self._get_route_start_end_times_line(start_time),
            *self._get_route_points_descriptions(start_time)
        ]

        for row in timetable:
            print(row)

        return timetable
