def display_menu(menu: list):
    """
    Выводит меню на экран
    :param menu: список словарей, name - название пункта меню, price - цена
    :return: Ничего не возвращает
    """
    print("Меню:")
    for i, item in enumerate(menu):
        print(f"  {i + 1}. {item['name']} - {item['price']} UAH")


def read_menu_item(menu: list) -> dict:
    """
    Считывает ввод пользователя и интепретирует его
    Если ввод - что-то из меню ресторана, то возвращает этот элемент меню
    Если введённого значения нету в меню - возвращает ошибку (пустой элемент)
    :param menu: список словарей, name - название пункта меню, price - цена
    :return: словарь элемент меню (пустой если ошибка)
    """
    user_input = input(f"Что вы желаете заказать? ")
    # проверяем что введена цифра
    try:
        user_input = int(user_input)
    except Exception:
        print('Введите, пожалуйста, пункт меню (цифрой).')
        return dict()
    # проверяем есть ли эта цифра в меню
    if 0 < user_input <= len(menu):
        return menu[user_input - 1]
    print('Введите, пожалуйста, пункт меню (цифрой) и показанных на экране!')
    return dict()


def is_client_ordering() -> int:
    """
    Спрашивает хочет ли клиент сделать заказ
    :return: возвращает 1 если хочет сделать заказ, возвращает 2 если хочет уйти и -1 если ввод неверный
    """
    print('1. Заказать')
    print('2. Выйти')
    user_input = input(f">>")
    # проверяем что введена цифра
    try:
        user_input = int(user_input)
    except Exception:
        print('Введите, пожалуйста, пункт меню (цифрой).')
        return -1
    # проверяем есть ли эта цифра в меню
    if user_input == 1:
        return 1
    elif user_input == 2:
        return 2
    else:
        print('Введите, пожалуйста, пункт меню (цифрой) и показанных на экране!')
        return -1


if __name__ == '__main__':
    # объявляем меню ресторана
    restaraunt_menu = [
        {"name": 'Кофе', "price": 18, "quantity": 100},
        {"name": 'Чай',  "price": 15, "quantity": 100},
        {"name": 'Какао', "price": 13, "quantity": 100},
        {"name": 'Булочка с вишней', "price": 10, "quantity": 100},
        {"name": 'Пончик с шоколадом', "price": 25, "quantity": 1},
        {"name": 'Пончик с кремом', "price": 25, "quantity": 3},
        {"name": 'Пончик с карамелью', "price": 25, "quantity": 3}
    ]
    # объявляем баланс клиента
    client_balance = 100

    while True:
        print(f"У вас на счету: {client_balance} UAH")
        # узнаем хочет ли клиент что-то заказать
        is_ordering = is_client_ordering()
        if is_ordering == 1:
            # клиент хочет что-то заказать
            # показываем меню
            display_menu(restaraunt_menu)
            # считываем выбор клиента
            chosen_item = read_menu_item(restaraunt_menu)
            # для отладки пишем что находится в нашем объекте
            # print(chosen_item)

            # не пустой словарь (корректный элемент меню)
            if chosen_item:
                # проверяем есть ли товар в наличии
                if chosen_item["quantity"] > 0:
                    # проверяем хватает ли у клиента денег
                    if client_balance >= chosen_item['price']:
                        # успешный заказ
                        print(f'Вот ваш заказ: {chosen_item["name"]}, c вашего счёта снято {chosen_item["price"]} UAH')
                        # снимаем деньги со счёта
                        client_balance -= chosen_item["price"]
                        # уменьшаем количество товара в запасе
                        chosen_item["quantity"] -= 1
                    else:
                        # не хватает денег
                        print(f'К сожалению, сумма на вашем счету: {client_balance} UAH'
                              f' недостаточно для оплаты {chosen_item["name"]} {chosen_item["price"]} UAH')
                else:
                    # нет товара в наличии
                    print(f'К сожалению, у нас закончились {chosen_item["name"]}. Приходите завтра :)')
            # пустой словарь
            else:
                pass
        # выход
        elif is_ordering == 2:
            exit(0)
