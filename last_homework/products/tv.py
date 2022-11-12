from .product import Product


class TV(Product):
    def __init__(self, diagonal: int, resolution: str, **kwargs):
        super().__init__(**kwargs)
        self.diagonal = diagonal
        self.resolution = resolution

        self.filter_fields.append('diagonal')
        self.filter_fields.append('resolution')

    def __str__(self):
        s = super().__str__()
        return s + f"""
    Diagonal: {self.diagonal}"
    Screen resolution: {self.resolution}"""
