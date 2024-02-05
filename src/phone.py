from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, sim_card_count: int) -> None:
        super().__init__(name, price, quantity)
        self.sim_card_count = sim_card_count

    def __add__(self, other):
        # return self.__class__(Phone).quantity + self.__class__(Item).quantity
        if isinstance(other, (Item, Phone)):
            return self.quantity + other.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.sim_card_count})"

    @property
    def number_of_sim(self):
        return self.sim_card_count
    @number_of_sim.setter
    def number_of_sim(self, number):
        if not isinstance(number, int) or number <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")

