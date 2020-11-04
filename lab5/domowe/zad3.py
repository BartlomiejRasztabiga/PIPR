def number_to_string_representation(num: int):
    numbers_map = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }

    zero = numbers_map[0]
    ones = list(map(lambda x: numbers_map[x], range(10)))
    tens = ["twenty", "thirty", "forty", "fifty"]

    # add all other numbers up to 59
    numbers_map.update(enumerate((tens_place if ones_place == zero
                                  else (f"{tens_place} {ones_place}")
                                  for tens_place in tens
                                  for ones_place in ones), len(numbers_map)))

    return numbers_map[num]


def get_hour_description(hour, minutes):
    assert 0 <= hour <= 12

    if minutes > 30:
        hour += 1

    return number_to_string_representation(hour)


def get_minutes_description(minutes):
    assert 0 <= minutes <= 60

    if minutes > 30:
        minutes = 60 - minutes

    if minutes == 15:
        return 'quarter'
    elif minutes == 30:
        return 'half'

    return f"{number_to_string_representation(minutes)} minutes"


def get_connective(minutes):
    if minutes == 0:
        return "o' clock"
    elif minutes <= 30:
        return "past"

    return "to"


def is_full_hour(minutes):
    return minutes == 0


def time_description(hour: int, minutes: int):
    hour_str = get_hour_description(hour, minutes)
    connective = get_connective(minutes)

    if is_full_hour(minutes):
        return f"{hour_str} {connective}"

    minutes_str = get_minutes_description(minutes)

    return f"{minutes_str} {connective} {hour_str}"


print(time_description(8, 15))
print(time_description(11, 13))
print(time_description(12, 30))
print(time_description(6, 37))
print(time_description(3, 45))
print(time_description(3, 0))
