def distance_along_axis(n, origin, destination):
    if not (-n <= origin <= n and -n <= destination <= n):
        raise ValueError("Coordinate out of range.")
    return min(abs(destination - origin), 2 * n - abs(destination - origin) + 1)
 
def distance(n, origin, destination):
    return distance_along_axis(n, origin[0], destination[0]) + distance_along_axis(n, origin[1], destination[1])

def time_of_fly(n, origin, destination, speed):
    pass