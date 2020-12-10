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


if __name__ == "__main__":
    warehouse = Warehouse()
    warehouse.add_resource(Resource('gliceryna', Amount(20, 'l')))
    warehouse.add_resource(Resource('aloes', Amount(15, 'l')))
    warehouse.add_resource(Resource('alkohol', Amount(1500, 'ml')))
    warehouse.print_warehouse_report()
