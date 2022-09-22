# list comprehension
x = [3, 5, 6]
# эти конструкции делают одно и то же, но одна из них имеет более короткую запись
# 1
comprehended_powered_x = [element ** 2 for element in x]
# 2
regular_powered_x = list()
for element in x:
    regular_powered_x.append(element ** 2)
print(comprehended_powered_x)
print(regular_powered_x)
#
new_list = [element for element in range(5, 100, 3)]
print(new_list)
print(list(range(5, 100, 3)))


# [*результат* for *называем имя итерируемого* in *то откуда берём элементы* *условие, какие элементы валидны*]

x = [3, 5, 7, 100, 150, 600]
comprehended_filtered_x = [element for element in x if element < 100]
# same thing but longer
regular_filtered_x = list()
for element in x:
    if element < 100:
        regular_filtered_x.append(element)
print(comprehended_filtered_x)
print(regular_filtered_x)

# Dictionary - словарь
# { *key1*: *value*, *key2*: *value*, ...}
d = {
    "я": "I",
    "Моё": "my",
    "Питон": "Python",
    "учусь": "to learn",
    "программировать": "to program",
    "на": "on",
}

# обращение к элементам словаря по ключу
print(d['учусь'])

# аналог списка
d = {
    0: 3,
    1: 4,
    2: 5
}
print(d[0], d[1], d[2])

# как можно удобно использовать словарь
d = {
    "name": "Coffee",
    "price": 18
}

print(type(d))

# методы объявления пустого словаря
d = dict()
d = {}
print(type(d))

d = {
    1: 'one',
    'one': 1
}

# добавление элементов в словарь
d['two'] = 2
d[2] = 'two'
print(d)

d = {
    "name": "Coffee",
    "price": 18
}
# все ключи словаря (то что перед :)
print(d.keys(), type(d.keys()), list(d.keys()))
# все значения словаря (то что после :)
print(d.values(), type(d.values()), list(d.values()))

print('Just dict')
for item in d:
    print('', item, d[item])

print('Dict keys (same as just dict)')
for item in d.keys():
    print('', item, d[item])

print('Dict values')
for item in d.values():
    print('', item)

# все ключи и значение словаря, объединённые в кортежи попарно
print(d.items(), type(d.items()), list(d.items()))
print('Dict items')
for item in d.items():
    print(item, item[0], item[1])

for key, value in d.items():
    print(key, value)

# итерация по символам строки
s = 'My name is 543'
for symbol in s:
    print(symbol)
