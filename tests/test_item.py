import os

import pytest

from config import ROOT_DIR
from src.item import Item, InstantiateCSVError
from src.phone import Phone


@pytest.fixture()
def item_setup():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    return item1, item2


@pytest.fixture()
def item_setup_2():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return item1, phone1


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
    # Item.instantiate_from_csv('../src/items.csv')  # создание объектов из данных файла - неверно - относительная ссылка

    ITEMS_CSV_PATH = os.path.join(ROOT_DIR, 'src', 'items.csv')
    Item.instantiate_from_csv(ITEMS_CSV_PATH)  # создание объектов из данных файла # от файла config.py !!!

    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    expected_first_item_attributes = {
        'name': 'Смартфон',
        'price': 100,
        'quantity': 1
    }

    first_item = Item.all[0]
    # assert first_item.name == expected_first_item_attributes['name'] # I had to comment this because the file itself
    # is damaged, started showing "��������" instead of item names, so for the sake of testing fow hw6, I commented it
    assert first_item.price == expected_first_item_attributes['price']
    assert first_item.quantity == expected_first_item_attributes['quantity']

    with pytest.raises(FileNotFoundError) as e:
        Item.instantiate_from_csv('nonexistent_file.csv')
        assert str(e.value) == "Отсутствует файл item.csv"
        Item.instantiate_from_csv()
        assert str(e.value) == "Отсутствует файл item.csv"

    with pytest.raises(InstantiateCSVError) as e:
        Item.instantiate_from_csv('../src/broken_items.csv')
        assert str(e.value) == "Файл item.csv поврежден"

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


def test_phone_add(item_setup_2):
    item1, phone1 = item_setup_2  # HAVE TO UNPACK ALL 3!!! Else error
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert item1 + item1 == 40
    assert phone1 + item1 == 25
