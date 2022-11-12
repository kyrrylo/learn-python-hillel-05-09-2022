from .product import Product


class Laptop(Product):
    def __init__(self, processor: str, ram: int, **kwargs):
        super().__init__(**kwargs)
        self.processor = processor
        self.ram = ram

        self.filter_fields.append('processor')
        self.filter_fields.append('ram')

    def __str__(self):
        s = super().__str__()
        return s + f"""
    Processor: {self.processor}"
    RAM: {self.ram}"""
