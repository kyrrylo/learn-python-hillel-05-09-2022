from employee import Employee
import locations


class Security(Employee):
    def __init__(self, name):
        super().__init__(
            name,
            'Security',
            working_locations=[
                locations.security_room.SecurityRoom.name,
                locations.warehouse.Warehouse.name
            ],
            unavailable_locations=[
                locations.kitchen.Kitchen.name,
                locations.client_zone.ClientZone.name
            ]
        )

    @staticmethod  # пишется над методами, которые не обращаются к self
    def say_hi_to(name):
        print(f'Hello, {name}')
