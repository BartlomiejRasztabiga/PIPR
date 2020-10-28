def get_intermediate_point(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x1+y1)/2, (x2+y2)/2)


print(get_intermediate_point((1, 2), (5, 6)))
