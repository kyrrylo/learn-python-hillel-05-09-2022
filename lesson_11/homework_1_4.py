"""
Написати програму, яка конвертує градуси у радіани (або навпаки, за бажанням, але вкажіть що саме обрали!). 180 градусів - це Pi радіан.
Написати програму, що конвертує гривню в доллар (або навпаки, за бажанням, але вкажіть що сами обрали!) по заданому в программі курсу. Округліть до двох цифр після крапки.
Написати програму, яка видаляє зі строки такі символи пунктуації: крапку, кому, крапку з комою, двокрапку, знаки оклику та питання.
Написати програму, яка приймає ціле число та відрізає від нього останню цифру. Наприклад: 10 -> 1, 100 -> 10, 25143 -> 2514
Написати програму, яка приймає ціле число та повідомляє яка в ньому остання цифра. Наприклад: 10 -> 0, 100 -> 0, 25143 -> 3
"""

import math


def radians_task():
    def to_radians(degrees: float, hello_message: str):
        print(hello_message)
        return math.radians(degrees)

    def to_degrees(radians: float):
        return math.degrees(radians)

    while True:
        try:
            what = int(input('Input 1 to convert into radians or 2 to convert into degrees: '))
            if what == 1:
                x = float(input('>'))
                return_value = to_radians(hello_message='hi', degrees=x)
                print(return_value)
            elif what == 2:
                x = float(input('>'))
                print(to_degrees(x))
            # print(math.radians(x))
            # print(math.degrees(x))
            # print(math.pi)
        except Exception:
            print('Input correct menu item or number please')


def uah_usd():
    while True:
        try:
            x = float(input('>'))
            print(round(x))
        except Exception:
            print('Input number please')


def replace_punctuation():
    s = 'Написати програму; ця програма видаляє зі строки такі символи пунктуації: крапку, кому, крапку з комою, двокрапку, знаки оклику та питання.'
    # base version
    s = s.replace(',', '').replace(';', '').replace(':', '')
    # version you could do now
    symbols_to_remove = [',', ':', ';']
    # для каждого symbol в symbols_to_remove:
    #   сделай с ним следующее
    # re.sub regular expression - тема Python Pro (или любого другого Веб-курсе)
    # translate & maketrans
    for symbol in symbols_to_remove:
        s = s.replace(symbol, '')
    print(s)


def cut_out():
    test_numbers = [10, 50, 122, 354781, -1343124, 123412]
    i_to_cut = 2
    for number in test_numbers:
        # print(number, str(number)[:len(str(number)) - i_to_cut])
        print(number, str(number)[:-i_to_cut], str(number)[-i_to_cut:])
        if number < 0:
            div, mod = divmod(abs(number), 10 ** i_to_cut)
            print(number, -div, mod)
        else:
            print(number, divmod(number, 10 ** i_to_cut))
        # % //


if __name__ == '__main__':
    # replace_punctuation()
    # cut_out()
    radians_task()
