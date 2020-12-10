import pytest

from main import Amount, UnknownUnitException, UnitConversionException


def test_wrong_unit():
    with pytest.raises(UnknownUnitException):
        Amount(1000, 'kg')


def test_good_unit():
    assert Amount(1000, 'l')


def test_conversion_to_l():
    amount = Amount(2, 'l')
    amount.convert_to('ml')

    assert amount.amount == 2000
    assert amount.unit_name == 'ml'


def test_conversion_to_ml():
    amount = Amount(2500, 'ml')
    amount.convert_to('l')

    assert amount.amount == 2.5
    assert amount.unit_name == 'l'


def test_wrong_conversion():
    amount = Amount(2500, 'ml')

    with pytest.raises(UnitConversionException):
        amount.convert_to('ml')


def test_wrong_conversion2():
    amount = Amount(2500, 'ml')

    with pytest.raises(UnknownUnitException):
        amount.convert_to('kg')
