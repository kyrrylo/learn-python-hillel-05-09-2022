import json
from products import Laptop, Mouse, Keyboard, TV

# объявляем константы, которые нам пригодятся
# имя файла с товарами
WAREHOUSE_FILENAME = 'warehouse.json'
# маппинг имён категорий к именам их классов
CLASSES_DICT = {
    "TV": TV,
    "Keyboard": Keyboard,
    "Mouse": Mouse,
    "Laptop": Laptop
}
# вступительное мега крутое (нет) слово
WELCOME_MESSAGE = """Hello from GigaChad MegaShop! Let's start shopping!"""
# список числовых полей к которым нужно применять ранжирование (больше/меньше), а не точное значение
NUMERIC_FIELDS = ["price", "ram"]


def load_warehouse() -> dict:
    """
    Загружает данные из файла-склада в объекты классов
    :return: список объектов-товаров
    """
    indices = dict()

    json_data = json.load(open(WAREHOUSE_FILENAME, mode='r'))
    for product_data in json_data['products']:
        product_category = product_data["category"]
        if product_category not in CLASSES_DICT:
            raise KeyError(f'Unknown category {product_category}')
        product_class = CLASSES_DICT[product_category]
        # пользуемся возможностями **kwargs, чтобы конвертировать словарь в параметры метода
        product_object = product_class(**product_data)
        for field_name, field_value in product_data.items():
            if field_name not in indices:
                indices[field_name] = dict()
            if field_value not in indices[field_name]:
                indices[field_name][field_value] = list()
            indices[field_name][field_value].append(product_object)
    return indices


def display_products(products_to_print: list):
    """
    Выводит на экран список товаров
    :param products_to_print: список товаров
    """
    for p in products_to_print:
        print(p)


def enumerated_choice(options):
    """
    Производит диалог с пользователем, где нужно узнать какое одно
    значение из представленных пользователь выберет
    :param options: доступные значения
    :return:
    """
    for i, key in enumerate(options):
        print(f'  {i+1}. {key.title()}')
    while True:
        # считываем ввод пользователя и интерпретируем его
        user_input = input('> ').lower()
        # ввод сходится с именем одного из значений
        if user_input in options:
            return user_input
        # ввод - порядковый номер значения
        elif user_input.isnumeric():
            list_index = int(user_input)
            if 0 < list_index <= len(options):
                # получаем само значение
                option = options[list_index-1]
                return option
        print('Please, provide valid input')


def filter_choice(fieldname: str, by_field: dict) -> list:
    """
    Проводит диалог с пользователем о выборе значения из доступных (для фильтра по нему)
    :param fieldname: названия поля по которому фильтруем
    :param by_field: индекс значений
    :return: список товаров удовлетворяющих выбранный фильтр
    """
    # просим пользователя выбрать значение нашего поля
    print(f'Please, choose {fieldname.title()}:')
    field_values = list(by_field.keys())
    # получаем выбор пользователя
    choice = enumerated_choice(field_values)
    # достаём список продуктов по имени значения
    return by_field[choice]


def user_dialog(indices: dict):
    print(WELCOME_MESSAGE)
    reset = True
    filtered_products = list()
    while True:
        if reset:
            filter_field = 'category'
            new_filtered_products = filter_choice(filter_field, indices[filter_field])
            display_products(new_filtered_products)
            if new_filtered_products:
                current_category = new_filtered_products[0].category
            else:
                current_category = 'Product'
            reset = False
        else:
            if filtered_products:
                example_product = filtered_products[0]
                print(f'Please, choose your filter:')
                filter_field = enumerated_choice(example_product.filter_fields)
                new_filtered_products = list()
                for new_product in filter_choice(filter_field, indices[filter_field]):
                    if new_product in filtered_products:
                        new_filtered_products.append(new_product)
                display_products(new_filtered_products)
                current_category = example_product.category
            else:
                new_filtered_products = list()
                current_category = 'Product'
        print(f'Found {len(new_filtered_products)} {current_category}(s).'
              f' Would you like to filter or reset?')
        choice = enumerated_choice(['Filter', 'Reset'])
        if choice == 'Filter':
            filtered_products = new_filtered_products
        elif choice == 'Reset':
            reset = True
        else:
            raise NotImplementedError(
                f'Method {enumerated_choice} returned {choice} when only Filter and Reset were valid options')


if __name__ == '__main__':
    shop_menu_indices = load_warehouse()
    user_dialog(shop_menu_indices)
