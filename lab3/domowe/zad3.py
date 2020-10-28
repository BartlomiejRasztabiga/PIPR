def fill_rectange_with_char(height, width, fill_char='#'):
    for _ in range(height):
        for _ in range(width):
            print(fill_char, sep='', end='')
        print() #newline


fill_rectange_with_char(3, 6)
