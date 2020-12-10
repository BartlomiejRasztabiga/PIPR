import pytest

from main import Amount, UnknownUnitException, Warehouse, Resource, Product


def test_wrong_unit():
    with pytest.raises(UnknownUnitException):
        Amount(1000, 'kg')


def test_good_unit():
    assert Amount(1000, 'l')


def test_add_amounts():
    amount1 = Amount(1000, 'ml')
    amount2 = Amount(2000, 'ml')
    assert amount1 + amount2 == Amount(3000, 'ml')


def test_add_amounts_different_names():
    amount1 = Amount(1000, 'ml')
    amount2 = Amount(2000, 'l')
    with pytest.raises(ValueError):
        amount1 + amount2


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


def test_conversion_same_name():
    amount = Amount(2500, 'ml')
    amount.convert_to('ml')

    assert amount.amount == 2500
    assert amount.unit_name == 'ml'


def test_conversion_no_persistence():
    amount = Amount(2500, 'ml')
    new_amount = amount.convert_to('l', persist=False)

    assert amount.amount == 2500
    assert amount.unit_name == 'ml'

    assert new_amount.amount == 2.5
    assert new_amount.unit_name == 'l'


def test_wrong_conversion():
    amount = Amount(2500, 'ml')

    with pytest.raises(UnknownUnitException):
        amount.convert_to('kg')


def test_create_warehouse():
    warehouse = Warehouse()
    warehouse.add_resource(Resource('gliceryna', Amount(20, 'l')))
    warehouse.add_resource(Resource('aloes', Amount(15, 'l')))
    assert len(warehouse.resources) == 2


def test_add_to_warehouse_duplicate():
    warehouse = Warehouse()
    warehouse.add_resource(Resource('gliceryna', Amount(20, 'l')))
    warehouse.add_resource(Resource('gliceryna', Amount(15, 'l')))
    assert len(warehouse.resources) == 1
    assert warehouse.resources[0].name == 'gliceryna'
    assert warehouse.resources[0].amount == Amount(35, 'l')


def test_create_product_with_requirements():
    requirements = [
        Resource('alkohol', Amount(600, 'ml')),
        Resource('gliceryna', Amount(150, 'ml')),
        Resource('aloes', Amount(350, 'ml')),
    ]
    product = Product('aloesowy żel do dezynfekcji rąk', requirements)

    assert len(product.requirements) == 3


def test_get_warehouse_report():
    warehouse = Warehouse()
    warehouse.add_resource(Resource('gliceryna', Amount(20, 'l')))
    warehouse.add_resource(Resource('aloes', Amount(15, 'l')))
    warehouse.add_resource(Resource('alkohol', Amount(1500, 'ml')))
    report = warehouse.get_warehouse_report()

    assert report
    print(report)
