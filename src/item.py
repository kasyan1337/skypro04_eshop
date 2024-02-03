import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        assert price >= 0, f"Price {price} should be more than 0"
        assert quantity >= 0, f"Quantity {quantity} should be more than 0"

        self.__name = name
        self.price = price
        self.quantity = quantity

        # Добавляем созданный экземпляр в список всех товаров
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            self.__name = name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_path=None):
        cls.all = []
        file_path = '../src/items.csv'
        with open(file_path, mode='r', encoding='windows-1251') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cls(name=row['name'], price=float(row['price']), quantity=int(row['quantity']))

    @staticmethod
    def string_to_number(number_str):
        number = int(float(number_str))
        return number

