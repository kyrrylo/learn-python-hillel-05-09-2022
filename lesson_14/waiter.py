from employee import Employee


class Waiter(Employee):
    def __init__(self, name):
        super().__init__(name, 'Waiter')
