from plant import Plant
from strawberry import Strawberry
from watermelon import Watermelon
# Наследование - класс-наследник повторяет все атрибуты (свойства) и методы (поведения) класса-предка.
#    при этом все наследники сохраняют принадлежность к типу предка, но не наоборот
#    (предок не принадлежит к типу наследников)
# Инкапсуляция - атрибуты класса принадлежат ему и должны меняться только изнутри класса.
#   Публичные можно смотреть, приватные недоступны даже для просмотра извне класса.
#   public - все могут смотреть и редактировать атрибуты объекта класса
#       (ПО УМОЛЧАНИЮ - ВСЕ АТРИБУТЫ ПАБЛИК)
#   protected - все наследники могут смотреть и редактировать атрибуты объекта класса
#       (ДОБАВИТЬ "_" ПЕРЕД ИМЕНЕМ АТРИБУТА)
#   private - только сам объект может смотреть и редактировать атрибуты класса
#       (ДОБАВИТЬ "__" ПЕРЕД ИМЕНЕМ АТРИБУТА)
# Полиморфизм - придавание методам с одним именем разного поведения в зависимости от класса, которому
#   это поведение принадлежит
#   например потомок класса Plant переопределяет метод grow, добавляя туда рост ягод (Strawberry)


def test_podorozhik():
    podorozhnik = Plant(name="Подорожник", speed=0.005, max_days=180)
    print(podorozhnik)
    podorozhnik.grow(7)
    print(podorozhnik)
    podorozhnik.grow(14)
    print(podorozhnik)
    podorozhnik.grow(180)
    print(podorozhnik)

    print(f'{isinstance(podorozhnik, Strawberry)=}')
    print(f'{isinstance(podorozhnik, Plant)=}')


def test_strawberry():
    s = Strawberry()
    print(s)
    s.grow(7)
    print(s)
    s.grow(3)
    print(s)
    s.grow(60)
    print(s)
    print(f'{type(s)=}')
    print(f'{isinstance(s, Strawberry)=}')
    print(f'{isinstance(s, Plant)=}')
    print(f'{isinstance(s, int)=}')
    print(f'{s.name=}')

    s.set_days(3)
    print(s)


if __name__ == '__main__':
    w = Watermelon('Watermelon', 0.5, 120)
    print(w)
    str_w = str(w)
    test_podorozhik()
    test_strawberry()
