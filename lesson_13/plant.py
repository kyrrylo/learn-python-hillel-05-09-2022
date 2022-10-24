class Plant:
    def __init__(self, name, speed, max_days):
        """
        Метод инициализации, в котором задаются поля/свойства/атрибуты класса
        и определяются их значения для этого объекта класса
        :param name: название растения
        :param speed: скорость роста
        :param max_days: сколько дней живёт
        """
        self.name = name
        # сколько дней прожило (текущее)
        self._days = 0
        # текущая высота в метрах
        self._height = 0
        # скорость роста
        self.speed = speed
        # флаг растет ли растение или уже умерло (влияет на поведение класса)
        self.to_grow = True
        # сколько дней может расти
        self.max_days = max_days

    def __str__(self):
        """
        :return: текстовое описание объекта класса
        """
        if self.to_grow:
            return f"{self.name} за {self._days} дней вырос(ла/ло) на {self._height} метров"
        else:
            return f"{self.name} рос(ла/ло) {self._days} дней и умерло"

    # расти за столько-то дней
    def grow(self, days):
        """
        Описание логики роста растения - изменение хронологии дней (__days) и роста (__height)
        Происходит проверка на умирание растения (max_days)
        :param days: на сколько дней растение подросло
        :return:
        """
        if self.to_grow:
            self._days += days
            self._height += self.speed * days
            self._height = round(self._height, 5)
            if self._days > self.max_days:
                self._height = round(self.speed * self.max_days, 5)
                self.die()

    def die(self):
        """
        Ставит флаг to_grow в отрицательно положение
        """
        self.to_grow = False
