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

        self.name = name
        self.price = price
        self.quantity = quantity

        # Добавляем созданный экземпляр в список всех товаров
        Item.all.append(self)


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