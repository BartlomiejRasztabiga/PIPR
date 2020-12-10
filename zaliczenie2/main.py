class UnknownUnitException(Exception):
    def __init__(self, unit):
        self.unit = unit


class UnitConversionException(Exception):
    pass


class Amount:
    def __init__(self, amount, unit_name):
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

    def convert_to(self, another_unit_name):
        if self.unit_name == another_unit_name:
            raise UnitConversionException()

        self._validate_unit_name(another_unit_name)

        new_amount = self.amount
        if another_unit_name == 'l' and self.unit_name == 'ml':
            new_amount /= 1000
        elif another_unit_name == 'ml' and self.unit_name == 'l':
            new_amount *= 1000

        self.amount = new_amount
        self.unit_name = another_unit_name

    @staticmethod
    def _validate_unit_name(unit_name):
        if unit_name not in ['l', 'ml']:
            raise UnknownUnitException(unit_name)


class Resource:
    def __init__(self, name, amount, unit='l'):
        self.name = name
        self.amount = amount
        self.unit = unit

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


class Product:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
