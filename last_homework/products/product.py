class Product:
    def __init__(self, name: str, price: float, quantity: int, category: str, brand: str):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.brand = brand

        self.filter_fields = ['name', 'price', 'brand']

    def __str__(self):
        return f"""{self.category} {self.name}
    {'in stock' if self.quantity > 0 else 'out of stock'}
    {round(self.price, 2)} UAH
    Brand: {self.brand}"""
