from src.item import Item


class LanguageMixin:
    def __init__(self, language='EN'):
        self.__language = language  # in this instance is self._language or self.__language better?

    def change_lang(self):
        self.__language = 'RU' if self.__language == 'EN' else 'EN'  # Can this be done by using __slots__?

    @property
    def language(self):
        return self.__language


class Keyboard(Item, LanguageMixin):

    def __init__(self, name: str, price: float, quantity: int, language='EN') -> None:
        Item.__init__(self, name, price, quantity)
        LanguageMixin.__init__(self, language)  # This did not work with super() being called twice.
        # Is there any advantage of using super() instead of directly calling the parent class?

    def __str__(self):
        return self.name
