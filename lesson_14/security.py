import logging
from employee import Employee


class Security(Employee):
    def __init__(self, name):
        super().__init__(name, 'Security')

    def check_in(self, location: str):
        if location == 'Кухня':
            logging.error('Охранник попытался войти на кухню')
            return
        super(Security, self).check_in(location)
