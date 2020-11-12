def get_product_name(product):
    return product['name']


def get_product_mass(product):
    return product['mass']


def get_total_weight_of_product(product_name, products):
    return sum(get_product_mass(product) for product in products if get_product_name(product) == product_name)


def get_total_weight_of_picles(products):
    return get_total_weight_of_product('ogórek', products)


products = []
print(get_total_weight_of_picles(products))
