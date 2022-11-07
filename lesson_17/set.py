# dict - значения, сгруппированные по ключам (ключи могут быть любым хэшируемом типом данных - строки, числа и классы с определённым методом __hash__()
def __hash__():
    pass
# list - перечень значений (доступны по индексу - целое число)
# tuple - то же что и список, но нельзя менять
# set - можно менять, перечеьн значений, но значения - уникальным

x = set()
print(x)
print(type(x))
x.add(5)
x.add(3)
x.add(4)
print(x)
x.add(5)
x.add('5')
x.add('a')
# cannot add unhashable
# x.add([1, 2, 3])
print(x)

x = {5, 4, '5', 3, 'a'}
print(type(x))
print(x)
# быстрое создание
x = {i for i in range(5)}
x.add(5)
x.add(3)
print(x)

# iterable тип данных - кортёж, список и множество (словарь тоже, но всегда есть пара значений)
x = [1, 2, 3, 3, 3, 4, 4, 5]
print(set(x))
print(tuple(x))

x = {5, 4, '5', 3, 'a'}
print(list(x))
print(tuple(x))
x = list(x)
x.append(5)
x.extend([4, 4, 3])
print(x)

# set specific methods
x = {5, 4, 3}
y = {1, 2, 3}
print(x.difference(y))
print(x.union(y))
print(x.intersection(y))