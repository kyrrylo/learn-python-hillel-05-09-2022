from employee import Employee


class Chief(Employee):
    def __init__(self, name):
        super().__init__(name, 'Chief')
