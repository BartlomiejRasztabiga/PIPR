import os
from typing import List


class UnknownUnitException(Exception):
    def __init__(self, unit):
        self.unit = unit


class UnitConversionException(Exception):
    pass


class Amount:
    def __init__(self, amount: int, unit_name: str):
        self.amount = amount
        self.unit_name = unit_name

    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, unit_name):
        self._validate_unit_name(unit_name)

        self._unit_name = unit_name

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    def __add__(self, other):
        if self.unit_name != other.unit_name:
            raise ValueError('Cannot add two amounts with different names')

        temp = Amount(self.amount, self.unit_name)
        temp.amount += other.amount
        return temp

    def __mul__(self, other):
        if not isinstance(other, int):
            raise ValueError('You can only multiply Amount by int')

        temp = Amount(self.amount, self.unit_name)
        temp.amount *= other
        return temp

    def __eq__(self, other):
        return self.amount == other.amount and self.unit_name == other.unit_name

    def convert_to(self, another_unit_name: str, persist=True):
        if self.unit_name == another_unit_name:
            # no conversion
            if not persist:
                return Amount(self.amount, another_unit_name)
            return

        self._validate_unit_name(another_unit_name)

        new_amount = self.amount
        if another_unit_name == 'l' and self.unit_name == 'ml':
            new_amount /= 1000
        elif another_unit_name == 'ml' and self.unit_name == 'l':
            new_amount *= 1000

        if persist:
            self.amount = new_amount
            self.unit_name = another_unit_name
        else:
            return Amount(new_amount, another_unit_name)

    @staticmethod
    def _validate_unit_name(unit_name):
        if unit_name not in ['l', 'ml']:
            raise UnknownUnitException(unit_name)


class Resource:
    def __init__(self, name: str, amount: Amount):
        self.name = name
        self.amount = amount

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    def __mul__(self, other):
        return Resource(self.name, self.amount * other)

    def __eq__(self, other):
        return self.name == other.name and self.amount == self.amount

    def __add__(self, other):
        return Resource(self.name, self.amount + other.amount)


class Warehouse:
    def __init__(self):
        self._resources = []

    def add_resource(self, resource: Resource):
        for _resource in self.resources:
            if _resource.name == resource.name:
                _resource.amount += resource.amount
                return

        self._resources.append(resource)

    @property
    def resources(self):
        return self._resources

    def get_warehouse_report(self):
        result = [
            f"| {'Zasób':<10} | {'Ilość w magazynie [l]':>21} |",
            f"| ---------- | --------------------- |"
        ]
        for resource in self.resources:
            amount_in_l = resource.amount.convert_to('l', persist=False).amount
            result.append(f"| {resource.name:<10} | {amount_in_l:>21} |")
        return result

    def print_warehouse_report(self):
        print(os.linesep.join(self.get_warehouse_report()))

    def get_resource_by_name(self, name):
        for resource in self.resources:
            if resource.name == name:
                return resource
        return None

    def are_enough_resources(self, requirements: List[Resource]):
        enough = True
        for requirement in requirements:
            resource = self.get_resource_by_name(requirement.name)
            own_amount_in_ml = resource.amount.convert_to('ml', persist=False)
            other_amount_in_ml = requirement.amount.convert_to('ml', persist=False)
            if other_amount_in_ml.amount > own_amount_in_ml.amount:
                enough = False
        return enough


class Product:
    def __init__(self, name, requirements: List[Resource]):
        self.name = name
        self.requirements = requirements

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def requirements(self):
        return self._requirements

    @requirements.setter
    def requirements(self, requirements):
        self._requirements = requirements


class OrderEntry:
    def __init__(self, product: Product, amount: int):
        self.product = product
        self.amount = amount

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, product):
        self._product = product

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount


class Order:
    def __init__(self, entries: List[OrderEntry]):
        self.entries = entries

    @property
    def entries(self):
        return self._entries

    @entries.setter
    def entries(self, entries):
        self._entries = entries

    def get_required_resources(self):
        requirements = []
        for entry in self.entries:
            amount = entry.amount
            product = entry.product
            product_requirements = product.requirements
            for requirement in product_requirements:
                order_requirement = requirement * amount
                requirements.append(order_requirement)

        # Here be dragons
        new_requirements = []
        added_requirements_names = set()
        for requirement in requirements:
            if requirement.name not in added_requirements_names:
                new_requirements.append(requirement)
                added_requirements_names.add(requirement.name)
            else:
                for _requirement in new_requirements:
                    if _requirement.name == requirement.name:
                        _requirement.amount += requirement.amount

        return new_requirements


class Factory:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, products):
        self._products = products
