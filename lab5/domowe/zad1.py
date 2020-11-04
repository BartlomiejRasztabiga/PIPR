def is_int(x):
    """ Returns True is string is an int. """
    try:
        int(x)
        return True
    except ValueError:
        return False


def get_valid_k_input(list_length):
    k = input('podaj k: ')

    if not is_int(k):
        print('podana wartość nie jest liczbą')
        return get_valid_k_input(list_length)

    k_int = int(k)

    if k_int <= 0 or k_int > list_length:
        print('podany indeks jest spoza dozwolonego zakresu')
        return get_valid_k_input(list_length)

    return k_int


def get_kth_element_reversed(lst):
    k = get_valid_k_input(len(lst))

    return lst[-k]


print(get_kth_element_reversed([1, 2, 3, 4, 5, 6, 7, 8, 9]))
