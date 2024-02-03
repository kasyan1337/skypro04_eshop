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
