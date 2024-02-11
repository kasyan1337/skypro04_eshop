import pytest

from src.item import Item
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


def test_phone_add(item_setup_2):
    item1, phone1 = item_setup_2  # HAVE TO UNPACK ALL 3!!! Else error
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert item1 + item1 == 40
    assert phone1 + item1 == 25


def test_phone_str(item_setup_2):
    item1, phone1 = item_setup_2
    assert str(phone1) == 'iPhone 14'


def test_phone_repr(item_setup_2):
    item1, phone1 = item_setup_2
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim(item_setup_2):
    item1, phone1 = item_setup_2
    assert phone1.number_of_sim == 2

    ### HERE IS TO TEST THE ERROR!

    with pytest.raises(ValueError) as e:  # Test raising of ValueError
        phone1.number_of_sim = 0
    assert str(e.value) == "Количество физических SIM-карт должно быть целым числом больше нуля"

    # Testing the successful set operation
    phone1.number_of_sim = 3
    assert phone1.number_of_sim == 3
