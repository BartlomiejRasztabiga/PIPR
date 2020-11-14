def biggest_subseries(series, length):
    return sorted(series, reverse=True)[:length]


print(biggest_subseries([6, 4, -8, 3, 9, 12, 2], 3))
