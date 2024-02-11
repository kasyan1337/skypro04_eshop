import csv


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

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        # from src.phone import \
        #     Phone  # Local import to avoid circular dependency (import error (most likely due to a circular import))
        # if isinstance(other, (Item, Phone)):
        # В Item тебе не нужен Phone, чтоб проверить можно ли их складывать,
        # достаточно проверить является ли other либо представителем Phone, либо его наследником

        if isinstance(other, Item):
            return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name[:10]

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
        with open(file_path, mode='r', encoding='windows-1251') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cls(name=row['name'], price=float(row['price']), quantity=int(row['quantity']))

    @staticmethod
    def string_to_number(number_str):
        number = int(float(number_str))
        return number
