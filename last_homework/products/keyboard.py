from .product import Product


class Keyboard(Product):
    def __init__(self, connection_type: str, backlight: bool, **kwargs):
        super().__init__(**kwargs)
        self.connection_type = connection_type
        self.backlight = backlight

        self.filter_fields.append('connection_type')
        self.filter_fields.append('backlight')

    def __str__(self):
        s = super().__str__()
        return s + f"""
    Connection: {self.connection_type}
    Keyboard backlight: {'Yes' if self.backlight else 'No'}"""
