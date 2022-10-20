# из *имя файла* импортировать *что импортируем*
from dog import Dog


if __name__ == '__main__':
    # создаём объект (instance) класса собака
    bob = Dog(name="Bob", age=4, breed="Немецкая овчарка")

    # проверяем что записалось и какой тип данных
    print(bob)
    print(type(bob))

    # создаём еще парочку собачек
    light = Dog(name="Light", age=6, breed="Корги")
    print(light)
    nick = Dog(name="Nick", age=3.5, breed="Алабай")
    print(nick)

    bob.say_woof()
    light.say_woof()
    nick.say_woof()

    bob.live_one_day()
    light.live_one_day()
    nick.live_one_day()

    # проверяем кто старше
    light > 20

    light > nick
    light.__gt__(nick)  # то же самое, строчка выше

    light < nick
    bob > light
    bob < light
    nick > bob
    nick < bob

    if 5 > 4:
        print(5, 'is greater than', 4)
    else:
        print(5, 'is lesser than', 4)
