import math
import time
import name_experiment

print(name_experiment.WEATHER)
print('Имя из lesson_2', __name__)


if __name__ == '__main__':
    t0 = time.time()
    # int - integer
    # целое число
    x1 = 9
    x2 = 2

    print(x1)
    print(type(x1) == int)
    print(type(x1))

    print(f'x1 + x2 =', x1 + x2)
    print(f'x1 - x2 =', x1 - x2)
    print(f'x1 * x2 =', x1 * x2)
    print(f'x1 / x2 =', x1 / x2, type(x1 / x2))
    print('Power')
    print(f'x1 ** 2 =', x1 ** 2)
    print(f'x1 ** (1 / 2)', x1 ** (1 / 2))
    print(f'pow(x1, 1 / 2)', pow(x1, 1 / 2))

    print('Division')
    print(f'{x1} // {x2} =', x1 // x2)
    print(f'{x1} % {x2} =', x1 % x2)
    print(f'divmod(x1, x2)', divmod(x1, x2))

    # float - плавающая запятая
    # floating point
    print('Дальше у нас float')
    y1 = 2.5618
    y2 = 6.13
    print(y1)
    print(f'Round 2: {round(y1, 2)}')
    # ceil - потолок
    print(f'Ceil: {math.ceil(y1)} type: {type(math.ceil(y1))}')
    # floor - пол
    print(f'Floor: {math.floor(y1)} type: {type(math.floor(y1))}')

    # вычитание и по модулю
    print(f'Subtract: {y1 - y2} absolute value: {abs(y1 - y2)}')
    print(f'Negative powers of 5: {-5 ** 2} {-5 ** 3} {-5 ** 999}')

    # time.sleep(5.05)
    print(f'Наша программа выполняется за: {round(time.time() - t0, 5)} секунд')

    # str - string - строка
    print('I live in Ukraine')
    print(str())
    print("I live in Ukraine")

    s = 'I live in Ukraine'
    print(s.lower())
    print(s.upper())
    s = 'python'
    print(s.upper(), s.upper().title())
    print(s.upper().capitalize(), s.capitalize())
    s = '''I live in Ukraine
I code on Python
My name is Kyrylo
    '''
    print('Обычный', s)
    print('title', s.title())
    print('capitalize', s.capitalize())
    print('upper', s.upper().isupper())
    print('lower', s.lower().islower())
    s = """I live in Ukraine
I code on Python
My name is Kyrylo
    """
    print(s)
    s = 'Python'
    print('Is digit', s, s.isdigit())

    print('Is digit', s, s.isdigit())
    print('Is numeric', s, s.isnumeric())
    print('Is decimal', s, s.isdecimal())
    print('Python__'.strip('_'))

    s = 'I am from Ukraine'
    s = s.replace('Ukraine', 'Kharkiv')
    # substring - подстрока

    print(s)
    s = 'you are from Ukraine, you are programmer'
    print(s.find('you'), s.rfind('you'))

    x = input('Введите число: ')
    # - может быть первым, а может и не быть
    # - может быть точка, но перед ней должно быть хотя бы одна цифра
    # - всё остальное должно быть цифрами
    try:
        int(x)
    except Exception:
        print('Это не число')