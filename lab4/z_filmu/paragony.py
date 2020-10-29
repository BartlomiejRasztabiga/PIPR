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
    return sum(price for name, price in receipt)


def format_price(price):
    price_zl, price_gr = split_price(price)
    return f"{price_zl}.{price_gr:02}"


my_receipt = [
    ("Bananas", 499),
    ("Oranges", 803),
    ("Milk", 315)
]

my_total_value = get_total_price(my_receipt)
print(format_price(my_total_value))
