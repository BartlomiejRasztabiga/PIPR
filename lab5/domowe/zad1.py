def is_int(x):
    """ Returns True is string is an int. """
    try:
        int(x)
        return True
    except ValueError:
        return False


def get_valid_k_input(list_length):
    while True:
        k = input('podaj k: ')

        if not is_int(k):
            print('podana wartość nie jest liczbą')
            continue

        k_int = int(k)

        if k_int <= 0 or k_int > list_length:
            print('podany indeks jest spoza dozwolonego zakresu')
            continue

        return k_int


def get_kth_element_reversed(lst):
    def get_kth_element_reversed_recursive(lst, current_k=0):
        if current_k == wanted_k:
            return lst[-current_k]
        return get_kth_element_reversed_recursive(lst, current_k + 1)

    list_length = len(lst)
    wanted_k = get_valid_k_input(list_length)

    return get_kth_element_reversed_recursive(lst)


print(get_kth_element_reversed([1, 2, 3, 4, 5, 6, 7, 8, 9]))
