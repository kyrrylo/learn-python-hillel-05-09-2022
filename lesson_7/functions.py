
def say_hi(name, small_talk):
    print(f'Hello, {name}! {small_talk}')
    # return None # по умолчанию добавляется пайтоном в конце каждой функции, если там нет другого ретурна


def say_bye(name, small_talk):
    print(f'Bye, {name}! {small_talk}')


def say_howdy(name, small_talk):
    print(f'How are you, {name}? {small_talk}')


def say_hi_to_str(name, small_talk):
    return f'Hello, {name}! {small_talk}'


"""
def имя функции(входные параметры через запятую или ничего):
    тело функции (с отступом)
    правильно в теле функции использовать только те переменные, которые:
        объявлены внутри тела функции 
        переданы как параметры (в круглых скобочках после имени функции)
        импортируемые библиотеки
    return некое значение (или ничего)
"""


def works_with_numbers(a: float, b: float, c: float, name: str) -> float:
    print(name, a ** 2, b ** 2, c)
    return (a ** 2 + b ** 2) / c

"""
Формат функции с подсказками типов
def имя функции(
    1-ый входной параметр: тип 1-го входного параметра,
    2-ый входной параметр: тип 2-го входного параметра...
) -> тип возвращаемого значения:
    тело функции
    return возвращаемое значение
"""

# scope - Область видимости, то, где имена переменных распознаются (видимы)
# в каждой функции - своя область видимости

if __name__ == '__main__':
    result_1 = say_hi('Python', 'Great weather!')
    print(result_1, type(result_1))
    print(None, type(None))

    say_hi_to_who = ['StrPython', 'StrPython5', 'StrPython8', 'Andrey']
    result_of_saying_hi = list()
    for who in say_hi_to_who:
        result_2 = say_hi_to_str(who, 'I had a great day, how about you?')
        result_of_saying_hi.append(result_2)
        print(result_2)

    print(result_of_saying_hi)
    link_to_function = say_hi
    print(link_to_function)
    print(type(link_to_function))
    linked_python_name = 'LinkedPython'
    link_to_function(linked_python_name, 'Great weather!')

    functions_to_call = [
        say_hi,
        say_howdy,
        say_bye
    ]
    user_name = input('What is your name? ')
    for func in functions_to_call:
        func(small_talk='Great weather!', name=user_name)

    result = works_with_numbers(2, 3, 2.5, 'divide (2^2 + 3^2) by 2,5')
    print(result)
    x = 4
    y = 3
    z = 2
    print(works_with_numbers(a=x, b=y, c=z, name=f'divide ({x}^2 + {y}^2) by {z}'))

