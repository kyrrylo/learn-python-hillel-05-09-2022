from .employee import Employee
from locations import Kitchen, Warehouse, SecurityRoom, ClientZone
import datetime


class Security(Employee):
    def __init__(self, name):
        super().__init__(
            name,
            'Security',
            working_locations=[
                SecurityRoom.name,
                Warehouse.name
            ],
            unavailable_locations=[
                Kitchen.name,
                ClientZone.name
            ]
        )
        self._weapon = 'Пистолет'

    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, value):
        if value != 'pistol' and value != 'machine gun':
            print('Оружие выбрано неверно')
            return
        self._weapon = value

    @weapon.deleter
    def weapon(self):
        time_now = datetime.datetime.now()
        if time_now.hour > 21:
            del self._weapon
        else:
            print('Еще не время складывать оружие')

    # get - получить
    def weapon_getter(self):
        return self._weapon

    # set - установить
    def weapon_setter(self, new_weapon):
        self._weapon = new_weapon

    def weapon_deleter(self):
        del self._weapon

    @staticmethod
    def another_say_hi_to(name):
        print(f'Hello, {name}')

    # @staticmethod  # пишется над методами, которые не обращаются к self
    @staticmethod
    def say_hi_to(name):
        print(f'Hello, {name}')
        # можно вызывать другие статик методы
        Security.another_say_hi_to(name)
        # а для вызова не-статик методов нужно создать объект этого класса,
        # который будет удалён по окончанию работы функции
        x = Security(name)
        x.not_static_say_hi_to(name)

    def not_static_say_hi_to(self, name):
        print(f'Hello, {self.name}')


# пример работы с декорторами property (getter), setter, deletter
if __name__ == '__main__':
    Security.say_hi_to('Bob')
    # попытка вызова динамического (не статик) метода без создания объекта класса выдаёт ошибку
    # Security.not_static_say_hi_to(name='Bob')
    rob = Security('Rob')
    # параметр селф можно подставить вручную и это будет работать
    # однако на практике так не делают - лучше дать пайтону самому подставить значение селф
    Security.not_static_say_hi_to(self=rob, name='Bob')

    print(rob.weapon_getter())
    rob.weapon_setter('пистолет')
    print(rob.weapon_getter())
    # выдаёт ошибку
    # rob.weapon_deleter()
    # print(rob.weapon_getter())

    print(rob.weapon)
    rob.weapon = 'knife'
    rob.weapon = 'pistol'
    print(rob.weapon)
    del rob.weapon
    print(rob.weapon)
