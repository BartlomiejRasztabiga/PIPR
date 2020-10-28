def format_val_with_fixed_decimal_point(val):
    return f"{val:.3f}"


def get_longest_string_length(strings):
    return max(map(lambda x: len(str(x)), strings))


def get_required_right_column_width(width_fixed_size, height_fixed_size, length_fixed_size):
    # 2 for padding on each side
    return get_longest_string_length([width_fixed_size, height_fixed_size, length_fixed_size]) + 2


def get_required_left_column_width(width_label, height_label, length_label):
    return get_longest_string_length([width_label, height_label, length_label]) + 2


def get_whitespace():
    return "#"


def get_padding_before_left_column_label():
    return get_whitespace()


def get_padding_after_left_column_label(required_left_column_width, padding_before_left_column_label, left_column_label):
    return get_whitespace() * \
        (required_left_column_width -
         len(padding_before_left_column_label) - len(left_column_label))


def get_padding_before_right_column_label(required_right_column_width, padding_before_right_column_label, right_column_label):
    return get_whitespace() * \
        (required_right_column_width -
         len(padding_before_right_column_label) - len(right_column_label))


def get_padding_after_right_column_label():
    return " "


def get_dimensions_table(width, height, length):
    table_rows = []

    width_fixed_size = format_val_with_fixed_decimal_point(width)
    height_fixed_size = format_val_with_fixed_decimal_point(height)
    length_fixed_size = format_val_with_fixed_decimal_point(length)

    # define labels
    width_label = "Szerokość"
    height_label = "Wysokość"
    length_label = "Długość"

    left_column_label = "Wymiar"
    right_column_label = "Wartość"

    # count how wide our columns should be
    required_right_column_width = get_required_right_column_width(
        width_fixed_size, height_fixed_size, length_fixed_size)

    required_left_column_width = get_required_left_column_width(
        width_label, height_label, length_label)

    # pre-calculate required paddings as strings with whitespaces
    padding_before_left_column_label = get_padding_before_left_column_label()
    padding_after_left_column_label = get_padding_after_left_column_label(
        required_left_column_width, padding_before_left_column_label, left_column_label)

    padding_after_right_column_label = get_padding_after_right_column_label()
    padding_before_right_column_label = get_padding_before_right_column_label(
        required_right_column_width, padding_after_right_column_label, right_column_label)

    print(required_right_column_width)

    header_row = f"{padding_before_left_column_label}{left_column_label}{padding_after_left_column_label}|{padding_before_right_column_label}{right_column_label}{padding_after_right_column_label}"
    print(header_row)


print(get_dimensions_table(10, 23, 5))
