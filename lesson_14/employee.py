import logging


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def check_in(self, location: str):
        logging.warning(f'{self.position}:: {self.name}:: used key-card at:: {location}')
