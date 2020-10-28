def get_space(): return " "


def get_frame_row(width, frame_char):
    return frame_char * width


def get_text_padding_row(width, frame_char):
    return frame_char + get_space() * (width - 2) + frame_char


def get_text_row(width, frame_char, text):
    return frame_char + f"{text:^{width-2}}" + frame_char


def print_frame_row(width, frame_char):
    print(get_frame_row(width, frame_char))


def print_text_padding_row(width, frame_char):
    print(get_text_padding_row(width, frame_char))


def print_text_row(width, frame_char, text):
    print(get_text_row(width, frame_char, text))


def print_string_in_frame(text, width, frame_char='*'):
    assert width >= len(text) + 2, "given width is too small to render frame correctly!"

    print_frame_row(width, frame_char)
    print_text_padding_row(width, frame_char)

    print_text_row(width, frame_char, text)

    print_text_padding_row(width, frame_char)
    print_frame_row(width, frame_char)


print_string_in_frame('HELLO', 11)
