import pytest

from src.item import Item


@pytest.fixture()
def item_setup():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    return item1, item2


def test_calculate_total_price(item_setup):
    # Unpack the items from the fixture
    item1, item2 = item_setup
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount(item_setup):
    # Unpack the items from the fixture
    item1, item2 = item_setup

    Item.pay_rate = 0.80
    item1.apply_discount()
    item2.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 16000

    # Reset items again for another test scenario
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    Item.pay_rate = 1
    item1.apply_discount()
    item2.apply_discount()
    assert item1.price == 10000
    assert item2.price == 20000

    # Reset items again for another test scenario
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    Item.pay_rate = 0.90
    item1.apply_discount()
    item2.apply_discount()
    assert item1.price == 9000
    assert item2.price == 18000


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    expected_first_item_attributes = {
        'name': 'Смартфон',  # Replace 'ExpectedName' with the actual expected name
        'price': 100,  # Replace with the actual expected price
        'quantity': 1  # Replace with the actual expected quantity
    }

    first_item = Item.all[0]
    assert first_item.name == expected_first_item_attributes['name']
    assert first_item.price == expected_first_item_attributes['price']
    assert first_item.quantity == expected_first_item_attributes['quantity']


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_name():
    item = Item('InitialName', 100, 1)
    item.name = "ahsgdausgfasugfuasgf"
    assert len(item.name) <= 10

    item.name = "akdds"
    assert len(item.name) == 5


def test_item_repr(item_setup):
    item1, item2 = item_setup
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('Ноутбук', 20000, 5)"


def test_item_str(item_setup):
    item1, item2 = item_setup
    assert str(item1) == 'Смартфон'
    assert str(item2) == 'Ноутбук'
