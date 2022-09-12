# ветвление, условия
# conditional expressions

a = 4
if 2 + 2 == a:  # если <некое условие>:
    print('Законы математики соблюдены')
else:  # иначе
    print('Математика не работает')

a = 5
b = 7
if a > b:
    print(f'{a} is greater than {b}')
else:
    print(f'{a} is lesser than {b}')

print(a > b)

g = True  # истинно
f = False  # ложно

print(f'{type(a < b)=}')
print(f'{g=} {type(g)=}')
print(f'{f=} {type(f)=}')

# если условное выражение не типа bool, то проверяется не-ноль или не-пустота
h = 0.0
if h:
    print('h is True')
else:
    print('h is False')

s = 'Python'
if s:
    print('s is True')
else:
    print('s is False')

color = 'blue'  # color
price = 8.0  # EUR
# logical operators логические операторы
if color == 'yellow':
    if price < 10:
        print('Вот так работает под капотом AND')

if color == 'yellow' and price < 10:  # логическое И
    print('Цена и цвет подходят! Можно брать!')
else:
    print('Или цена или цвет не подходят')

menu = 'булочка, чай, кофе'
# ручной пример логического ИЛИ (знать стоит, писать так не стоит)
# in - в, оператор членства: есть ли что-то в чем-то
if 'кофе' in menu.lower():
    print('В меню есть то, что нам нужно')
else:
    if 'какао' in menu.lower():
        print('В меню есть то, что нам нужно')
    else:
        print('В этом меню нету ни кофе, ни какао')

# рекомендумый пример логического ИЛИ
# lazy-check ленивая проверка
if 'кофе' in menu.lower() or 'какао' in menu.lower() or 100 / 0:  # логическое ИЛИ
   print('В меню есть то, что нам нужно')
else:
   print('В этом меню нету ни кофе, ни какао')

# расстояние Левенштайна - как работают поисковики на исправление

menu = 'булочка, чай, зеленый чай, черный чай, кофе'
# оператор ELIF - else-if вторичное условие, которое проверяется после того как первичное условие не было выполнено
if 'кофе' in menu.lower():
    print('Заказываю кофе!')
elif 'какао' in menu.lower():
    print('Заказываю какао!')
elif 'горячий шоколад' in menu.lower():
    print('Заказываю горячий шоколад!')
elif 'травяной чай' in menu.lower():
    print('Заказываю травяной чай')
elif 'черный чай' in menu.lower():
    print('Заказываю черный чай')
elif 'зеленый чай' in menu.lower():
    print('Заказываю зелёный чай')
else:
    print('Дайте тогда воды..')

print(f'{s=}; {s == "Javascript"=}')  # оператор равенства
print(f'{s=}; {s != "Javascript"=}')  # оператор неравенства
print(f'{a=}; {b=}; {a == b=}')
print(f'{a < b=}; {a <= b=}; {a > b=}; {a >= b=}')  # больше/меньше или равно
b = 5
print(f'{b=}; {a <= b=}; {a < b=}; {a >= b=}; {a > b=}; {a == b=}')  # больше/меньше или равно
print(f'{a != b=}; {not a == b=}; {not True=}; {not False=}')
# not - обратное от булевого значения
print(f'{"script" in "Javascript"=}; {"script" in "C++"=}; {"script" in "JavascriPt"=}')




