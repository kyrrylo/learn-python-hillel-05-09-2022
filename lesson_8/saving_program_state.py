import json
import os
from datetime import datetime


def input_number(comment):
    """
    Считывает у пользователя число, конвертирует его во float и возвращает
    :param comment: комментарий к вводу числа
    :return: считанное число
    """
    while True:
        try:
            x = float(input(comment))
            return x
        except Exception:
            print('Введите число!')


def input_calculate(a: float, b: float) -> (float, str):
    """
    Принимает два числа, считывает арифметическую операцию у пользователя и возвращает её результат
    :param a: первое число
    :param b: второе число
    :return:
        сложение, вычитание, умножение или деление двух чисел
        тип оператора строкой
    """
    while True:
        operator = input('Введите +, -, * или /:')
        if operator == '+':
            return a + b, operator
        elif operator == '-':
            return a - b, operator
        elif operator == '*':
            return a * b, operator
        elif operator == '/':
            return a / b, operator
        else:
            print('Введите оператор!')


state_filename = 'state.json'
if os.path.isfile(state_filename):
    history = json.load(open(state_filename))  # load - загрузить
else:
    history = []

while True:
    a = input_number('a=')
    b = input_number('b=')
    result, operator = input_calculate(a, b)
    result_string = f'{a} {operator} {b} = {result}'
    print(result_string)
    history.append({
        'date': datetime.now().strftime('%Y-%b-%d %H:%M:%S'),
        'equation': result_string
    })
    user_choice = input('Хотите посмотреть историю? (y)')
    if user_choice.lower() == 'y' or user_choice.lower() == 'yes':
        print(history)
    user_choice = input('Хотите выйти? (y/n)')
    if user_choice.lower() == 'y' or user_choice.lower() == 'yes':
        break
json.dump({"history": history[-5:]}, open(state_filename, mode='w'), indent=4)  # dump - сохранить
