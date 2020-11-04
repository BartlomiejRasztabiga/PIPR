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


def time_description(hour: int, minutes: int):
    pass


print(number_to_string_representation(0))
# print(number_to_string_representation(15))
# print(number_to_string_representation(60))
# print(number_to_string_representation(32))
# print(number_to_string_representation(17))
