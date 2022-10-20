class Dog:
    def __init__(self, name: str, age: float, breed: str):  # initialization
        # поля или атрибуты класса
        self.name = name
        self.age = age
        self.breed = breed

    # вместо "функция" говорим "метод"
    # поведение класса, его возможности
    def say_woof(self):
        print(f'A dog of {self.breed} breed and name {self.name} says "Woof!"')

    def live_one_day(self):
        output_str = 'Весело то как жить собаке с человеком!'
        if self.breed == 'Корги':
            output_str += f' Похоже, теперь вокруг много шерсти...может это {self.name}?'
        elif self.breed == 'Алабай':
            output_str += f' Похоже, теперь вокруг всё в чьих-то слюнях...может это {self.name}?'
        print(output_str)

    def __str__(self):
        return f'Собака {self.name}, {self.breed}, {self.age} лет'

    def older_message(self, other):
        print(f'{self.name} старше {other.name}, потому что ей {self.age} лет, а {other.name} - {other.age}')

    def younger_message(self, other):
        print(f'{self.name} младше {other.name}, потому что ей {self.age} лет, а {other.name} - {other.age}')

    def __gt__(self, other) -> bool:  # greater than, >
        if isinstance(other, Dog):
            if self.age > other.age:
                self.older_message(other)
                return True
            else:
                self.younger_message(other)
                return False
        elif isinstance(other, int):
            print('Собака не может быть числооооом!')

    def __lt__(self, other) -> bool:  # lesser than, <
        if isinstance(other, Dog):
            if self.age < other.age:
                self.younger_message(other)
                return True
            else:
                self.older_message(other)
                return False


if __name__ == '__main__':
    random_dog = Dog(name='Random', age=-5, breed='Unknown')
    print(random_dog)
