from datetime import date


def split_price(price):
    price_zl = price // 100
    price_gr = price % 100
    return price_zl, price_gr


def get_description(name, price):
    return f"Price of {name} is {format_price(split_price(price))}"


def print_description(name, price):
    description = get_description(name, price)
    print(description)


def get_product():
    product_name = input("Podaj nazwe produktu: ")
    product_price = input("Podaj cene produktu w groszach: ")
    return product_name, int(product_price)


def get_total_price(receipt):
    """
    given receipt of products
    outputs sum of their prices
    """
    return sum(price for name, price in receipt)


def format_price(price):
    price_zl, price_gr = split_price(price)
    return f"{price_zl}.{price_gr:02}"


def print_product(product, current_position):
    name, price = product
    price = format_price(price)
    tax_group = get_tax_group(name)
    print(f"{current_position:2}. {name:20}{price:>6}{tax_group:>2}")


def print_receipt(date, receipt):
    """
    1. output date
    2. for each element in receipt output that element
    3. output line
    4. output summary
    """
    if len(receipt) == 0:
        print("Receipt is empty")
        return

    print(date)
    current_position = 1
    for name, price in receipt:
        print_product((name, price), current_position)
        current_position += 1
    print('-' * 32)
    total_value = get_total_price(receipt)
    formatted_value = format_price(total_value)
    print(f"TOTAL: {formatted_value:>23}")


def get_tax_group(product_name):
    tax_group_A = {'Milk', 'Bread'}
    tax_group_B = {'Bananas', 'Oranges'}

    if product_name in tax_group_A:
        return 'A'
    elif product_name in tax_group_B:
        return 'B'
    return 'E'


my_receipt = [
    ("Bananas", 49999),
    ("Oranges", 803),
    ("Milk", 3155),
    ("Lollipop", 100)
]

print_receipt(str(date.today()), my_receipt)
