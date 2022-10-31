from employee import Employee
import locations


class Chief(Employee):
    def __init__(self, name):
        super().__init__(
            name,
            'Chief',
            working_locations=[
                locations.kitchen.Kitchen.name,
                locations.warehouse.Warehouse.name
            ],
            unavailable_locations=[
                locations.security_room.SecurityRoom.name,
                locations.client_zone.ClientZone.name
            ]
        )
