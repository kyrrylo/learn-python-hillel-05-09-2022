from .employee import Employee
from locations import Kitchen, Warehouse, SecurityRoom, ClientZone


class Chief(Employee):
    def __init__(self, name):
        super().__init__(
            name,
            'Chief',
            working_locations=[
                Kitchen.name,
                Warehouse.name
            ],
            unavailable_locations=[
                SecurityRoom.name,
                ClientZone.name
            ]
        )
