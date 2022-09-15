# define - определять
def add(a, b):
    # def <имя функции>(<перечень параметров>):
    # далее - тело функции с отсупом 4 пробела
    print('function')
    # return - вернуть, результат работы функции
    return a + b


print('not function')
x = add('java', 'script')
print(x)

c = 'my'
d = 'string'
print(c + ' ' + d)
print()
print('a', '\n', 'b', 'c', 'd', 4, 2, 3, 4, 5, 6, 7, 2, sep='-', end='...\n\n')


def my_function(variable_name, input_phrase='Введите число'):
    # argument - параметр функции
    return float(input(f'>>{input_phrase} {variable_name}: '))


print(my_function('x'))
print(my_function('z', input_phrase='Input number'))
print(my_function('у', input_phrase='Введіть число'))


def add_everything_numeric(*args, my_str):
    sum = 0
    for x in args:
        sum = sum + x
    print(my_str)
    return sum


def add_everything_str(*args, z='выводится на экран в конце тела функции'):
    sum = ''
    print(len(args))  # length
    for x in args:
        sum = sum + x
    print(z)
    return sum

print(add_everything_numeric(2, 3, 4, 5, 6, my_str='выводится на экран в конце тела функции'))
print(add_everything_str('a', 'b', 'c', 'd', 'e', z='выводится на экран в конце тела функции'))


# используя return
def add_menu_item_return(menu):
    new_item = input('Введите название нового элемента: ')
    new_item_price = input('Введите его цену: ')
    # menu = menu + '\n' + new_item + ' ' + new_item_price
    menu += '\n' + new_item + ' ' + new_item_price
    # menu = menu + f'\n {new_item} {new_item_price}'
    return menu


# используя global мы можем менять значения внешних переменных
def add_menu_item_global():
    global menu
    new_item = input('Введите название нового элемента: ')
    new_item_price = input('Введите его цену: ')
    menu += '\n' + new_item + ' ' + new_item_price


# для чтения внешних переменных объявлять global не нужно
def display_menu():
    print(f'Меню:{menu}')
    print("""
1. Добавить новый элемент в меню
2. Пригласить клиента
3. Выход
""")


menu = ''
while False:
    # вывести информацию пользователю
    display_menu()
    # считать выбор пользователя
    x = input(">> Введите пункт меню (1-3): ")
    # логика реагирования на выбор
    # варианты выбора
    if x == '1':
        add_menu_item_global()
    elif x == '2':
        pass
    elif x == '3':
        break


DEGREE_SUM_TRIANGLE = 180


def read_triangle_vertice(name: str) -> float:
    while True:
        x = input(f'{name}=')
        try:
            x = float(x)
        except Exception:
            print('Это не число!')
            continue  # - вернуться в начало цикла (на следующую его итерацию)
        if x > 0:
            return x
        else:
            print('Это число не может быть стороной треугольника!')


def does_triangle_exist(a: float, b: float, c: float) -> bool:
    if a + b > c and a + c > b and b + c > a:
        print("Треугольник существует")
        return True
    else:
        print("Треугольник не существует")
        return False


# периметр треугольника
def triangle_perimeter(a: float, b: float, c: float) -> float:
    return a + b + c


# площадь треугольника
# Type Annotation - заметки в заголовке функции, позволяющие программистам понимать что на входе
# Это не влияет на интерпретацию кода (если передаётся число, а ожидается строка, ошибки не будет)
# ошибка будет тогда, когда мы воспользуемся переменной не как этим типом, а не от самого объявления
def triangle_square(a: float, b: float, c: float) -> float:
    p = triangle_perimeter(a, b, c) / 2
    square = pow(p * (p - a) * (p - b) * (p - c), 0.5)
    return square


print('#' * 10)
print('Проверка существования треугольника')
print('#' * 10)
a = read_triangle_vertice('a')
b = read_triangle_vertice('b')
c = read_triangle_vertice('c')
if does_triangle_exist(a, b, c):
    perimeter = triangle_perimeter(a, b, c)
    print(f"Периметр треугольника: {perimeter}")
    print(f"Площадь треугольника: {triangle_square(a, b, c)}", file=open('square_output.txt', 'w'))
    if perimeter > 10000:
        print(f'Периметр этого треугольника больше периметра моего двора!')

# PEP 8
# MyStr - CamelCase - в классах (далі буде)
# my_str - snake_case - переменные и функции
# MY_STR - uppercase snake_case - для констант

x = [2, 3, 4]
print(type(x), x)
