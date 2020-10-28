def get_common_section(segment1, segment2):
    a1, b1 = segment1
    a2, b2 = segment2

    # segment has to be in a form (a, b) where a <= b
    assert a1 <= b1
    assert a2 <= b2

    are_intersecting = b1 >= a2 and b2 >= a1
    assert are_intersecting, "given segments are not intersecting!"

    left_boundary = max(a1, a2)
    right_boundary = min(b1, b2)

    return (left_boundary, right_boundary)


print(get_common_section((10, 15), (12, 16)))
print(get_common_section((10, 12), (12, 15)))
print(get_common_section((1, 1), (1, 1)))
print(get_common_section((1, 2), (2, 3)))
print(get_common_section((1,5), (7, 10)))