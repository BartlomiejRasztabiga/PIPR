def is_number_tryexcept(s):
    """ Returns True is string is a number. """
    try:
        int(s)
        return True
    except ValueError:
        return False


def get_kth_element_reversed(lst):
    k = input('podaj k: ')

    if not is_number_tryexcept(k):
        raise ValueError("podana wartość nie jest liczbą")

    k_int = int(k)

    if k_int <= 0 or k_int > len(lst):
        raise ValueError("podany indeks jest spoza dozwolonego zakresu")

    return lst[-k_int]


print(get_kth_element_reversed([1, 2, 3, 4, 5, 6, 7, 8, 9]))
