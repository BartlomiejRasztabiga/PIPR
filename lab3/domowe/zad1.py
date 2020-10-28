def get_common_section(section1, section2):
    a1, b1 = section1
    a2, b2 = section2

    # section has to be in a form (a, b) where a <= b
    assert a1 <= b1
    assert a2 <= b2

    are_intersecting = b1 >= a2 and b2 >= a1

    left_boundary = max(a1, a2) if are_intersecting else -1
    right_boundary = min(b1, b2) if are_intersecting else -1

    return (left_boundary, right_boundary)


print(get_common_section((10, 12), (13, 15)))
print(get_common_section((10, 15), (12, 16)))
print(get_common_section((10, 12), (12, 15)))
print(get_common_section((1, 1), (1, 1)))
print(get_common_section((12, 15), (1, 2)))
print(get_common_section((1, 2), (2, 3)))