def function(a, b):
    return a + b


print(1, end=';\n', sep='-')
print(1, 2, end=';\n', sep='-')
print(1, 2, 3, end=';\n', sep='-')
print(1, 2, 3, 4, end=';\n', sep='-')


def narg_function(*args, **kwargs):
    print(args)
    print(kwargs)
    # print(type(args))
    our_sum = sum(args)
    if kwargs['to_print']:
        print(our_sum)
    return our_sum


narg_function(1, to_print=False, not_to_print=20)
narg_function(1, 2, to_print=True)
narg_function(1, 2, 3, to_print=False)
narg_function(1, 2, 3, 4, to_print=True)


class Product:
    def __init__(self, **kwargs):
        self.a = kwargs['a']
        self.b = kwargs['b']
        self.category = kwargs['category']
        self.d = kwargs.get('d', 5)


class TV(Product):
    def __init__(self, e: int, f: str, **kwargs):
        super().__init__(category='TV', **kwargs)
        self.e = e
        self.f = f

    def __str__(self):
        return f"{self.a=} {self.b=} {self.category=} {self.d=} {self.e=} {self.f=}"

menu = list()

for elem in json:
    dict_from_json = {
        "name": "Samsungus",
        "price": 15000,
        "diagonal": 48
    }
    tv = TV(a=dict_from_json["name"], b=dict_from_json["price"], d="", e=dict_from_json["diagonal"], f="")
    print(tv)
    menu.append(elem)

class Iron(Product):
    def __init__(self, ):
        pass

b = TV(e="", f="Not so much F", a=3, b=3)
b.e = "Very E"
print(b)
