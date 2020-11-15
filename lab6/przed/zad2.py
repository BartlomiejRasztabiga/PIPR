def distance(n, point1, point2):
    point1_x, point1_y = point1
    point2_x, point2_y = point2

    if abs(point1_x) >= n or abs(point1_y) >= n or abs(point2_x) >= n or abs(point2_y) >= n:
        raise ValueError("coords are not from given range")

    dist_x = min(abs(point1_x - point2_x), point1_x + (n - point2_x))
    dist_y = min(abs(point1_y - point2_y), point1_y + (n - point2_y))

    return dist_x + dist_y
