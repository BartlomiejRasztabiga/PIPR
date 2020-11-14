def distance(n, point1, point2):
    point1_x, point1_y = point1
    point2_x, point2_y = point2

    return abs(point1_x - point2_x) + abs(point1_y - point2_y)