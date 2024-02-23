from src.item import Item

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv()
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv('../src/broken_items.csv') # If I left this blank
    # it would not find the file in the first place let alone check it, so I created a new one and had to edit main.py
    # InstantiateCSVError: Файл item.csv поврежден
