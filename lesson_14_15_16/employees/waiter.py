from .employee import Employee
from locations import Kitchen, Warehouse, SecurityRoom, ClientZone


class Waiter(Employee):
    def __init__(self, name):
        super().__init__(
            name,
            'Waiter',
            working_locations=[
                Kitchen.name,
                ClientZone.name
            ],
            unavailable_locations=[
                SecurityRoom.name,
                Warehouse.name
            ]
        )
