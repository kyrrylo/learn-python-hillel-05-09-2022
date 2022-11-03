import logging


class Employee:
    def __init__(self, name: str, position: str, working_locations: list, unavailable_locations: list):
        self.name = name
        self.position = position
        # композиция 1 объекта класса Logger
        self.logger = logging.getLogger(f"{self.position} - {self.name}")
        self.logger.setLevel(logging.INFO)
        # логика посещений
        # композиция N объектов классов из package (пакет) locations
        self.working_locations = working_locations
        self.unavailable_locations = unavailable_locations

    def check_in(self, location: str):
        if location in self.working_locations:
            self.logger.info(location)
        elif location in self.unavailable_locations:
            self.logger.error(location)
        else:
            self.logger.warning(location)
