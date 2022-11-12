from .product import Product


class Mouse(Product):
    def __init__(self, connection_type: str, button_count: int, **kwargs):
        super().__init__(**kwargs)
        self.connection_type = connection_type
        self.button_count = button_count

        self.filter_fields.append('connection_type')
        self.filter_fields.append('button_count')

    def __str__(self):
        s = super().__str__()
        return s + f"""
    Connection: {self.connection_type}
    Buttons: {self.button_count}"""
