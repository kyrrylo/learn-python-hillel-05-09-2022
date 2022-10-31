from employee import Employee
import locations


class Waiter(Employee):
    def __init__(self, name):
        super().__init__(
            name,
            'Waiter',
            working_locations=[
                locations.kitchen.Kitchen.name,
                locations.client_zone.ClientZone.name
            ],
            unavailable_locations=[
                locations.security_room.SecurityRoom.name,
                locations.warehouse.Warehouse.name
            ]
        )
