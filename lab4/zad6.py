def get_value_range_and_avg_value(value_tuple):
    avg_value = sum(value_tuple) / len(value_tuple)
    value_range = (min(value_tuple), max(value_tuple))

    return (value_range, avg_value)

print(get_value_range_and_avg_value((2, -5)))