class Product:
    def __init__(self, name: str, price: float, quantity: int, category: str, brand: str):
        """
        Класс товара, наследуется более конкретными товарами
        Структура для хранения информации о товаре
        :param name: название товара
        :param price: цена товара
        :param quantity: количество на складе, наличие
        :param category: категория товара (определяется классами-наследниками)
        :param brand: название брэнда
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.brand = brand

        # храним по каким полям нужно фильтровать, а по каким нет
        self.filter_fields = ['name', 'price', 'brand']

    def __str__(self):
        return f"""{self.category} {self.name}
    {'in stock' if self.quantity > 0 else 'out of stock'}
    {round(self.price, 2)} UAH
    Brand: {self.brand}"""
