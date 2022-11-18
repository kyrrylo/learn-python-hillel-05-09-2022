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
NUMERIC_FIELDS = ["price", "ram", "diagonal"]


def load_warehouse() -> dict:
    """
    Загружает данные из файла-склада
    Создаёт объекты классов
    Распихивает ссылки на объекты классов по индексам на каждое поле
    :raises KeyError: в случае если в файле-складе указана неизвестная категория
    :return: индексы
    """
    # объявляем финальный словарь индексов по полям товаров
    indices = dict()

    # открываем файл-склад и проходимся по каждому элементу там
    json_data = json.load(open(WAREHOUSE_FILENAME, mode='r'))
    for product_data in json_data['products']:
        # получаем категорию продукта
        product_category = product_data["category"]
        # распознаём категорию и создаём новый объект соответствующего класса
        if product_category not in CLASSES_DICT:
            raise KeyError(f'Unknown category {product_category}')
        product_class = CLASSES_DICT[product_category]
        # пользуемся возможностями **kwargs, чтобы конвертировать словарь в параметры метода
        product_object = product_class(**product_data)
        # добавляем данные объекте в индекс по каждому полю
        for field_name, field_value in product_data.items():
            # создаём под-индекс для имени поля
            if field_name not in indices:
                indices[field_name] = dict()
            # под-под список для перечня объектов с таким значением поле (по которому индекс)
            # запустите в режиме отладки, чтобы посмотреть на структуру этого индекса
            # она проще чем кажется на первый взгляд)
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
    :return: выбранное значение
    """
    # выводим на экран пронумерованные доступные варианты
    for i, key in enumerate(options):
        print(f'  {i+1}. {key}')
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


def input_number(context_str: str) -> float:
    x = input(context_str)
    while True:
        try:
            x = float(x)
            return x
        except Exception:
            x = input('Please, input number: ')

def filter_num_choice(fieldname: str, by_field: dict) -> list:
    """
    Проводит диалог с пользователем, в ходе которого по числовому полю
    фильтруются товары (вхождение в диапазон/рамку)
    :param fieldname: имя поля
    :param by_field: индекс по этому значению
    :return: список товаров, удовлетворяющий введённому диапазону
    """
    # считываем верхнюю и нижнюю границы
    lower = input_number(f'Please, choose lower value of {fieldname.title()}: ')
    upper = input_number(f'Please, choose upper value of {fieldname.title()}: ')
    # подготавливаем список подходящих товаров
    qualifying_products = list()
    # проходимся по индексу
    for value, products in by_field.items():
        # если группа товаров удовлетворяет условию, то добавляем их
        if lower <= value <= upper:
            qualifying_products.extend(products)
    return qualifying_products


def get_unique_values_from_products(fieldname: str, products: list) -> list:
    """
    Собирает уникальные значения поля fieldname по товарам,
     чтобы по ним потом пользователь мог фильтровать
    :param fieldname: имя поля
    :param products: список продуктов
    :return: список уникальных значений поля по этим продуктам
    """
    # перечисляем все возможные значения
    # намеренно пропускаем числовые (NUMERIC_FIELDS) потому как их здесь быть не должно
    if fieldname == 'name':
        unique_values = {p.name for p in products}
    elif fieldname == 'brand':
        unique_values = {p.brand for p in products}
    elif fieldname == 'processor':
        unique_values = {p.processor for p in products}
    elif fieldname == 'resolution':
        unique_values = {p.resolution for p in products}
    elif fieldname == 'connection_type':
        unique_values = {p.connection_type for p in products}
    elif fieldname == 'backlight':
        unique_values = {p.backlight for p in products}
    elif fieldname == 'button_count':
        unique_values = {p.button_count for p in products}
    else:
        raise NotImplementedError(f'Unexpected {fieldname} encountered')
    return list(unique_values)


def filter_choice(fieldname: str, by_field: dict, provided_products: list) -> list:
    """
    Проводит диалог с пользователем о выборе значения из доступных (для фильтра по нему)
    :param fieldname: названия поля по которому фильтруем
    :param by_field: индекс по этому значению
    :param provided_products: товары, которые уже есть в списке
                            (следует исключить общие значения полей, ориентируясь
                             только на контекст товаров в этом списке)
                             если пустой список, значит ориентироваться ни на что не нужно
    :return: список товаров удовлетворяющих выбранный фильтр
    """
    if fieldname in NUMERIC_FIELDS:
        return filter_num_choice(fieldname, by_field)
    # просим пользователя выбрать значение нашего поля
    print(f'Please, choose {fieldname.title()}:')
    # фильтруем только значения полей в контексте текущих товаров
    if provided_products:
        # получаем список допустимых значений
        field_values = get_unique_values_from_products(fieldname, provided_products)
    # если же контекста текущих товаров нет, то просто берём все значения по этому полю
    else:
        field_values = list(by_field.keys())
    # получаем выбор пользователя
    choice = enumerated_choice(field_values)
    # достаём список продуктов по имени значения
    return by_field[choice]


def user_dialog(indices: dict):
    print(WELCOME_MESSAGE)
    # флаг режима работы - фильтруем дальше или же откатываемся к выбору категории
    reset = True
    # список отфильтрованных (на текущий момент) товаров
    filtered_products = list()
    # задаём имя по умолчанию для категории (для общения с пользователем)
    current_category = 'Product'
    # будущий список отфильтрованных товаров (которые подготавливаем к показу)
    new_filtered_products = list()
    while True:
        # режим "откат"
        if reset:
            # осуществляем диалог по фильтру категории
            filter_field = 'category'
            # задаём будущий список отфильтрованных товаров
            new_filtered_products = filter_choice(filter_field, indices[filter_field], list())
            # отображаем товары
            display_products(new_filtered_products)
            # фиксируем имя текущей категории если список не пустой
            if new_filtered_products:
                current_category = new_filtered_products[0].category
            # выключаем режим отката
            reset = False
        # режим не-отката
        else:
            # если товаров в списке нет, то и фильтровать нечего
            if filtered_products:
                # берём первый продукт из списка, исходя из логики программы - все объекты будут одного класса
                example_product = filtered_products[0]
                print(f'Please, choose your filter:')
                # обращаемся к полю в классе, где мы задаём по каким полям можно фильтровать
                # узнаём у пользователя по какому полю нужно фильтровать
                filter_field = enumerated_choice(example_product.filter_fields)
                # задаём новый список отфильтрованных товаров (которые подготавливаем к показу)
                new_filtered_products = list()
                # совмещаем фильтр с уже существующими товарами в списке - только при совпадении отображаем
                # тут лучше использовать set(), однако для списков длиной <20 можно и списком
                for new_product in filter_choice(filter_field, indices[filter_field], filtered_products):
                    if new_product in filtered_products:
                        new_filtered_products.append(new_product)
                # отображаем дофильтрованные товары
                display_products(new_filtered_products)
                current_category = example_product.category
        # вне зависимости от режима отката/не отката, спрашиваем у пользователя куда двигаться дальше
        print(f'Found {len(new_filtered_products)} {current_category}(s).'
              f' Would you like to filter or reset?')
        choice = enumerated_choice(['Filter', 'Reset'])
        # если фильтруем дальше, то необходимо зафиксировать текущий список товаров
        if choice == 'Filter':
            filtered_products = new_filtered_products
        # если откатываем, то включаем отвечающий за это флаг
        elif choice == 'Reset':
            reset = True
        # не будем до конца доверять нашему методу enumerated_choice и вставим сообщение об ошибке
        # которое укажет на неё в случае возникновения (пока неизвестно каком, однако мы к нему готовы)
        else:
            raise NotImplementedError(
                f'Method {enumerated_choice} returned {choice} when only Filter and Reset were valid options')


if __name__ == '__main__':
    shop_menu_indices = load_warehouse()
    user_dialog(shop_menu_indices)
