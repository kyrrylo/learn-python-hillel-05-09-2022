class A:
    def __init__(self, brand):
        self.brand = brand


list_a = [A('Samsung'), A('LG'), A('')]

for a in list_a:
    print(a.__getattribute__('brand'))
