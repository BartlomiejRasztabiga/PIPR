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


def get_product_price(name):
    product_prices = {
        'Bananas': 499,
        'Oranges': 1803,
        'Milk': 315,
        'Lollipop': 100,
        'Bread': 509,
    }

    if name in product_prices:
        return product_prices[name]
    else:
        return -1


def get_product_value(name, quantity):
    return get_product_price(name) * quantity


def get_product_tax_value(name, quantity):
    return round(get_product_value(name, quantity) * get_tax_percentage(name))


def get_product():
    name = input("Podaj nazwe produktu: ")
    quantity = input("Podaj ilosc produktu: ")

    total_value = get_product_value(name, quantity)

    return name, total_value


def get_total_price(receipt):
    """
    given receipt of products
    outputs sum of their prices
    """
    return sum(get_product_value(name, quantity) for name, quantity in receipt)


def get_total_tax(receipt):
    """
    given receipt of products
    outputs sum of their tax values
    """
    return sum(get_product_tax_value(name, quantity) for name, quantity in receipt)


def get_total_plus_tax(receipt):
    return get_total_price(receipt) + get_total_tax(receipt)


def format_price(price):
    price_zl, price_gr = split_price(price)
    return f"{price_zl}.{price_gr:02}"


def print_product(product, current_position):
    name, quantity = product

    total_price = format_price(get_product_value(name, quantity))

    tax_group = get_tax_group(name)
    print(f"{current_position:2}. {name:20}{total_price:>6}{tax_group:>2}")


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
    for name, quantity in receipt:
        print_product((name, quantity), current_position)
        current_position += 1
    print('-' * 32)

    total_value = get_total_price(receipt)
    formatted_value = format_price(total_value)

    total_tax = get_total_tax(receipt)
    formatted_tax = format_price(total_tax)

    total_plus_tax = get_total_plus_tax(receipt)
    formatted_total_plus_tax = format_price(total_plus_tax)

    print(f"TAX: {formatted_tax:>25}")
    print(f"TOTAL: {formatted_value:>23}")
    print(f"TOTAL+TAX: {formatted_total_plus_tax:>19}")


def get_tax_percentage(product_name):
    tax = {
        'A': 0.12,
        'B': 0.08,
        'E': 0.22
    }

    tax_group = get_tax_group(product_name)
    if tax_group in tax:
        return tax[tax_group]
    else:
        return 0


def get_tax_group(product_name):
    tax_group_A = {'Milk', 'Bread'}
    tax_group_B = {'Bananas', 'Oranges'}

    if product_name in tax_group_A:
        return 'A'
    elif product_name in tax_group_B:
        return 'B'
    return 'E'


my_receipt = [
    ("Bananas", 1),
    ("Oranges", 1),
    ("Milk", 1),
    ("Lollipop", 1)
]

print_receipt(str(date.today()), my_receipt)
