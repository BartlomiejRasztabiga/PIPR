def number_to_string_representation(num: int):
    zero = "zero"
    ones = [zero, "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine"]
    tens = ["twenty", "thirty", "forty", "fifty"]

    numbers = ones + ["ten", "eleven", "twelve", "thirteen", "fourteen",
                      "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    numbers.extend(tens_place
                   if ones_place == zero else (tens_place + "-" + ones_place)
                   for tens_place in tens for ones_place in ones)

    return numbers[num]


def get_hour_description(hour, minutes):
    assert 0 <= hour <= 12

    h = hour
    if minutes > 30:
        h += 1

    return number_to_string_representation(h)


def get_minutes_description(minutes):
    assert 0 <= minutes <= 60

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


def time_description(hour: int, minutes: int):
    hour_str = get_hour_description(hour, minutes)
    connective = get_connective(minutes)

    if minutes == 0:
        return f"{hour_str} {connective}"

    minutes_str = get_minutes_description(
        minutes if minutes <= 30 else 60 - minutes)

    return f"{minutes_str} {connective} {hour_str}"


print(time_description(8, 15))
print(time_description(11, 13))
print(time_description(12, 30))
print(time_description(6, 37))
print(time_description(3, 45))
print(time_description(3, 0))
