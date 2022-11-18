from .product import Product


class Laptop(Product):
    def __init__(self, processor: str, ram: int, **kwargs):
        """
        Товар категории ноутбук
        :param processor: процессор устройства
        :param ram: объём оперативной памяти
        :param kwargs: параметры для базового класса, которые в него передаются
        """
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
