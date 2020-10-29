def split_price(price):
    price_zl = price // 100
    price_gr = price % 100
    return (price_zl, price_gr)


def get_description(name, price):
    price_zl, price_gr = split_price(price)
    return f"Price of {name} is {price_zl}.{price_gr:02}"


def print_description(name, price):
    description = get_description(name, price)
    print(description)


def get_product():
    product_name = input("Podaj nazwe produktu: ")
    product_price = int(input("Podaj cene produktu w groszach: "))
    return product_name, product_price


product = get_product()
name, price = product
print_description(name, price)
