from typing import List


def get_average_of(collection):
    return sum(collection) / len(collection)


def count_elements_above_average(collection):
    collection_average = get_average_of(collection)
    print([x for x in collection if x >= collection_average])
    return len([x for x in collection if x >= collection_average])


def count_elements_above_average_in_collections(collections):
    result = []
    for collection in collections:
        try:
            res = count_elements_above_average(collection)
        except ZeroDivisionError:
            res = 'DZIELENIE PRZEZ ZERO'
        except TypeError as e:
            print(e)
            res = 'ZŁA WARTOŚĆ'

        result.append(res)
    return result


print(count_elements_above_average_in_collections(
    [[1, 2, 3], [5, 6, 7], [], [3, 4, 5], ["12a", 1, 4]]))
