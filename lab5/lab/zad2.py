def get_kth_element_reversed(list):
    k = int(input('podaj k: '))
    assert k > 0 and k <= len(list)
    return list[-k]

print(get_kth_element_reversed([1,2,3,4,5,6,7,8,9]))