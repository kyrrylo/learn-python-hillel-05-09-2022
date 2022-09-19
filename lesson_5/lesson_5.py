"""
int() - целое число
float() - десятичное число
str() - строка
bool() - условное выражение
"""

x = [
    5,
    6,
    7.0,
    'my name is',
    [0, 2, True]
]
print(x)
print(type(x))

# самый простой способ обращаться к элементам списка
print(x[0])  # первый элемент (программисты ведь с ноля считают)
print(x[1])  # второй элемент
print(x[-1])  # последний элемент
print(x[-2])  # предпоследний элемент

# print(x[5])  # ошибка! Вне диапазона этого списка

print(f'Длина списка {len(x)}')  # length - длина

element = [4, 3, 2]
y = [4, 5, -5, 5000, 43, 40]
# динамическая по-элементная операция над списком
# не зависит от его длины
for element in y:  # для каждого element в списке y
    print(element ** 2, end=', ')

print('\n', y)


y = [4, 5, -5, 5000, 43, 40]
y_in_power_of_two = list()  # пустой список
# динамическая по-элементная операция над списком
# не зависит от его длины
for element in y:  # для каждого element в списке y
    processed_element = element ** 2
    y_in_power_of_two.append(processed_element)  # добавить в конец

print(y, y_in_power_of_two)

# вручную посчитать сумму элементов в списке
y = [2, -7, -5, 975, 60, -400, 847580, -53463, 0]
summa = 0
for element in y:
    summa += element  # оператор накапливания (increment)
print(summa)
# посчитать сумму встроенным методом пайтона
print(sum(y))

# ручное итерирование
iterator = 0
processed_y = list()
for element in y:
    print(f'{element} это {iterator}-ый элемент списка')
    if iterator < 4:
        processed_element = element - 100
    else:
        processed_element = element + 100
    processed_y.append(processed_element)
    iterator += 1
print(f'Было: {y}')
print(f'Стало: {processed_y}')

# итерирование встроенным методом пайтона
for element in enumerate(y):
    print(f'{element[1]} это {element[0]}-ый элемент списка')

# предварительное раскрытие tuple, когда мы знаем количество элементов
for i, value in enumerate(y):
    print(f'{value} это {i}-ый элемент списка')

y[0] = 77
print(y)

# tuple - кортеж
# tuple во многом похожи на списки. Основное отличие - мы не можем изменить их размер и значение элементов
# вот так с кортежами можно
t = (5, 7, 12)
print(len(t))
print(sum(t))
print(t[-1])
print(t[0])

# а вот так нельзя
# t[0] = 55
# t.append(55)

t = tuple([5, 7, 12, 'python', False])
converted_tuple = list(t)
converted_tuple[0] = 55
print(t)
print(converted_tuple)

##
print(type(t))
print(isinstance(t, tuple))
if isinstance(t, tuple):  # является ли t типом tuple
    t = list(t)
t[0] = -2

x = [6, 8, 22, 'my string']
if isinstance(x, str):
    print(x.capitalize())
elif isinstance(x, int):
    print(x / 5)
else:
    print(x)

if x:
    # хотя бы один элемент в списке, неважно какой - True
    print('x is True')
else:
    # пустой список это False
    print('x is False')

x = [4, 6, 2, -5, 81]
print(f'{min(x)=}')
print(f'{max(x)=}')

print(sorted(x))  # сортирует, возвращает сортированное, а сам список не меняет
print(x)
x.sort()  # сортирует, меняя список
print(x)

print(sorted(x, reverse=True))  # сортировка в обратном порядке

sack_of_fruits = [
    ("яблоко", 20),
    ("Груша", 25),
    ("арбуз", 1500),
    ("клубника", 5),
]
print(sack_of_fruits)


def get_fruit_weight(element):
    return element[1]


print('Сортировка по весу', sorted(sack_of_fruits, key=get_fruit_weight))
print('min', min(sack_of_fruits, key=get_fruit_weight))
print('max', max(sack_of_fruits, key=get_fruit_weight))


def get_fruit_name(element):
    return element[0].lower()

print('Сортировка по названию', sorted(sack_of_fruits, key=get_fruit_name))
# print('Сортировка по названию', sorted(sack_of_fruits, key=get_fruit_name, reverse=True))  # можно в обратном порядке
print('min', min(sack_of_fruits, key=get_fruit_name))
print('max', max(sack_of_fruits, key=get_fruit_name))

import os


for filename in os.listdir():
    if '.py' not in filename:
        os.remove(filename)

# slice
x = [1, 2, 3, 4, 5, 6, 70, 80, 90, 100]
print(len(x))
print(x[:4])  # с начала и до четвёртого
print(x[5:])  # с пятого и до конца
print(sorted(sack_of_fruits, key=get_fruit_weight, reverse=True)[:3])

print(x[:101])  # устойчивы к ошибкам (в отличии от индексов)
print(x[::2])  # от начала до конца, но с шагом 2 (каждый второй вместо каждого)
print(x[1::2])  # от первого и до конца, но с шагом 2
print(x[::9])  # шаг тоже устойчив к ошибкам

print(x[:-1])  # от начала и до последнего
print(x[-2:])  # от предпоследнего и до конца

x = [1, 2, 3, 4, 5, 6, 70, 80, 90, 10]
print(x[::-1])  # простой способ получить обратный список (и кого-то удивить)

x.reverse()
print(x)
print(x[::-2])

x = [1, 2, 3, 4, 5, 6, 70, 80, 90, 10]
i = 0
while i < len(x):
    element = x[i]
    # do something
    print(element)
    i += 1

x = [
    5,
    6,
    7.0,
    'my name is',
    [0, 2, True]
]
print(x[-1][-2])
# изменять список внутри tuple можно, а заменять - нет
t = (1, 2, 3, [2, 3, 4])
t[-1][1] = -1
t[-1].append(5)
print(t)
# t[-1] = [2, -1, 4]  # а так всё еще нельзя

print(list(range(10)))  # диапазон от 0 до 10 (исключая 10, т.е. до 9)
print(list(range(10, 1000)))  # диапазон от 10 до 1000 (исключая 1000, т.е. до 999)
print(list(range(10, 1000, 5)))  # диапазон от 10 до 1000 с шагом 5, всё так же исключая 1000 (10, 15...990, 995)

for i in range(0, 10, 2):
    print(i)

for i in (3, 4, 2):
    print(x[i])

# antipattern, так лучше не делать
for i in range(len(x)):
    print(x[i])

# List Comprehension (наступне заняття)
x = [i for i in range(10)]
print(x)